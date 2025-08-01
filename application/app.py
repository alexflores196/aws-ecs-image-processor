import os
import boto3
import uuid
from flask import Flask, render_template, request, redirect, url_for, send_file, abort, session, jsonify
from PIL import Image
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-super-secret-key-for-dev')

S3_BUCKET = os.environ.get('S3_BUCKET_NAME')
DYNAMODB_TABLE_NAME = os.environ.get('DYNAMODB_TABLE_NAME')

if not S3_BUCKET or not DYNAMODB_TABLE_NAME:
    raise ValueError("Required environment variables S3_BUCKET_NAME or DYNAMODB_TABLE_NAME are not set.")

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

@app.route('/')
def index():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

    session_id = session['session_id']
    images = []
    try:
        prefix = f"{session_id}/thumbnails/"
        response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=prefix)

        if 'Contents' in response:
            for thumb in response['Contents']:
                thumb_key = thumb['Key']
                original_filename = os.path.basename(thumb_key).replace('thumb-', '')
                full_original_key = f"{session_id}/{original_filename}"

                db_response = table.get_item(Key={'ImageKey': full_original_key})
                item_data = db_response.get('Item', {})

                if item_data:
                    images.append({
                        'thumbnail_url': s3.generate_presigned_url('get_object', Params={'Bucket': S3_BUCKET, 'Key': thumb_key}, ExpiresIn=3600),
                        'original_url': s3.generate_presigned_url('get_object', Params={'Bucket': S3_BUCKET, 'Key': full_original_key}, ExpiresIn=3600),
                        'original_key': full_original_key,
                        'basic_metadata': item_data.get('BasicMetadata', {}),
                        'enhanced_metadata': item_data.get('EnhancedMetadata', {})
                    })
    except Exception as e:
        print(f"Error retrieving data: {e}")
        images = []

    return render_template('index.html', images=images, has_images=(len(images) > 0))

@app.route('/upload', methods=['POST'])
def upload():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    session_id = session['session_id']

    files = request.files.getlist('files')
    if not files:
        return redirect(url_for('index'))

    for file in files:
        if file and file.filename != '':
            try:
                file_extension = os.path.splitext(file.filename)[1]
                unique_filename = f"{str(uuid.uuid4())}{file_extension}"
                upload_key = f"{session_id}/{unique_filename}"
                s3.upload_fileobj(file, S3_BUCKET, upload_key, ExtraArgs={"ContentType": file.content_type})
            except Exception as e:
                print(f"Error uploading file {file.filename}: {e}")

    return redirect(url_for('index'))

@app.route('/api/images')
def api_images():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

    session_id = session['session_id']
    images = []

    try:
        prefix = f"{session_id}/thumbnails/"
        response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=prefix)

        if 'Contents' in response:
            for thumb in response['Contents']:
                thumb_key = thumb['Key']
                original_filename = os.path.basename(thumb_key).replace('thumb-', '')
                full_original_key = f"{session_id}/{original_filename}"

                db_response = table.get_item(Key={'ImageKey': full_original_key})
                item_data = db_response.get('Item', {})

                if item_data:
                    images.append({
                        'thumbnail_url': s3.generate_presigned_url('get_object', Params={'Bucket': S3_BUCKET, 'Key': thumb_key}, ExpiresIn=3600),
                        'original_url': s3.generate_presigned_url('get_object', Params={'Bucket': S3_BUCKET, 'Key': full_original_key}, ExpiresIn=3600),
                        'original_key': full_original_key,
                        'basic_metadata': item_data.get('BasicMetadata', {}),
                        'enhanced_metadata': item_data.get('EnhancedMetadata', {})
                    })

    except Exception as e:
        print(f"Error in /api/images: {e}")
        return jsonify([]), 500

    return jsonify(images)

@app.route('/convert')
def convert():
    try:
        key = request.args.get('key')
        target_format = request.args.get('format', 'jpeg').lower()
        width = request.args.get('width', type=int)
        height = request.args.get('height', type=int)

        if not key:
            abort(400, 'Missing image key')

        response = s3.get_object(Bucket=S3_BUCKET, Key=key)
        image_bytes = response['Body'].read()

        base_name = os.path.splitext(os.path.basename(key))[0]

        if target_format == 'pdf':
            from PIL import Image as PilImage
            pdf_buffer = io.BytesIO()
            c = canvas.Canvas(pdf_buffer, pagesize=letter)
            image_reader = ImageReader(io.BytesIO(image_bytes))
            pil_img = PilImage.open(io.BytesIO(image_bytes))
            img_width, img_height = pil_img.size
            max_width, max_height = letter
            scale = min(max_width / img_width, max_height / img_height)
            new_width = img_width * scale
            new_height = img_height * scale
            x = (max_width - new_width) / 2
            y = (max_height - new_height) / 2
            c.drawImage(image_reader, x, y, width=new_width, height=new_height, preserveAspectRatio=True, mask='auto')
            c.showPage()
            c.save()
            pdf_buffer.seek(0)
            return send_file(
                pdf_buffer,
                as_attachment=True,
                download_name=f"{base_name}_converted.pdf",
                mimetype='application/pdf'
            )

        img = Image.open(io.BytesIO(image_bytes))
        if width and height:
            img = img.resize((width, height), Image.Resampling.LANCZOS)

        if img.mode == 'RGBA' and target_format == 'jpg':
            img = img.convert('RGB')

        buffer = io.BytesIO()
        img_format_pil = 'JPEG' if target_format == 'jpg' else target_format.upper()
        img.save(buffer, format=img_format_pil)
        buffer.seek(0)

        return send_file(
            buffer,
            as_attachment=True,
            download_name=f"{base_name}_converted.{target_format}",
            mimetype=f'image/{target_format}'
        )
    except Exception as e:
        print(f"Error converting image: {e}")
        abort(500, 'Error during image conversion')

@app.route('/delete', methods=['POST'])
def delete():
    try:
        key_to_delete = request.form['key']
        session_id, original_filename = key_to_delete.split('/', 1)
        thumb_key_to_delete = f"{session_id}/thumbnails/thumb-{original_filename}"

        s3.delete_object(Bucket=S3_BUCKET, Key=key_to_delete)
        s3.delete_object(Bucket=S3_BUCKET, Key=thumb_key_to_delete)
        table.delete_item(Key={'ImageKey': key_to_delete})
    except Exception as e:
        print(f"Error deleting image: {e}")
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear():
    if 'session_id' in session:
        session_id = session['session_id']
        s3_paginator = s3.get_paginator('list_objects_v2')
        pages = s3_paginator.paginate(Bucket=S3_BUCKET, Prefix=f"{session_id}/")
        for page in pages:
            if 'Contents' in page:
                objects_to_delete = [{'Key': obj['Key']} for obj in page['Contents']]
                s3.delete_objects(Bucket=S3_BUCKET, Delete={'Objects': objects_to_delete})
                with table.batch_writer() as batch:
                    for obj in objects_to_delete:
                        batch.delete_item(Key={'ImageKey': obj['Key']})
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)