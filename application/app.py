import os
import boto3
import uuid
from flask import Flask, render_template, request, redirect, url_for, send_file, abort, session
from PIL import Image
import io

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
                original_key = os.path.basename(thumb_key).replace('thumb-', '')
                full_original_key = f"{session_id}/{original_key}"

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

    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        try:
            # --- NEW: Generate a unique filename ---
            # Get the file extension (e.g., .png, .jpg)
            file_extension = os.path.splitext(file.filename)[1]
            # Create a new unique filename
            unique_filename = f"{str(uuid.uuid4())}{file_extension}"
            
            # Prepend the session_id to the unique filename
            upload_key = f"{session_id}/{unique_filename}"
            
            s3.upload_fileobj(file, S3_BUCKET, upload_key, ExtraArgs={"ContentType": file.content_type})
        except Exception as e:
            print(f"Error uploading to S3: {e}")
    return redirect(url_for('index'))

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
        img = Image.open(io.BytesIO(image_bytes))

        if width and height:
            img = img.resize((width, height), Image.Resampling.LANCZOS)
        
        buffer = io.BytesIO()
        img_format_pil = 'JPEG' if target_format == 'jpg' else target_format.upper()
        
        if img.mode == 'RGBA' and (img_format_pil == 'JPEG'):
             img = img.convert('RGB')

        img.save(buffer, format=img_format_pil)
        buffer.seek(0)
        
        base_name = os.path.splitext(os.path.basename(key))[0]
        download_name = f"{base_name}_converted.{target_format}"

        return send_file(
            buffer,
            as_attachment=True,
            download_name=download_name,
            mimetype=f'image/{target_format}'
        )
    except Exception as e:
        print(f"Error converting image: {e}")
        abort(500, 'Error during image conversion')

# --- NEW: Delete Route for a single image ---
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

# --- NEW: Clear Route for the entire session ---
@app.route('/clear', methods=['POST'])
def clear():
    if 'session_id' in session:
        session_id = session['session_id']
        # Delete all objects for this session from S3
        s3_paginator = s3.get_paginator('list_objects_v2')
        pages = s3_paginator.paginate(Bucket=S3_BUCKET, Prefix=f"{session_id}/")
        for page in pages:
            if 'Contents' in page:
                for obj in page['Contents']:
                    s3.delete_object(Bucket=S3_BUCKET, Key=obj['Key'])
                    table.delete_item(Key={'ImageKey': obj['Key']})
    
    session.clear() # Clear the user's session cookie
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)