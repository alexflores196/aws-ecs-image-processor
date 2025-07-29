import boto3
import os
from PIL import Image, ExifTags
import io
import json

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
DYNAMODB_TABLE_NAME = os.environ.get('DYNAMODB_TABLE_NAME')
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

def get_exif_data(image):
    exif_data = {}
    try:
        exif = image._getexif()
        if exif:
            for tag, value in exif.items():
                decoded_tag = ExifTags.TAGS.get(tag, tag)
                exif_data[str(decoded_tag)] = str(value)
    except Exception:
        pass
    return exif_data

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # --- NEW: Parse the session_id and filename from the key ---
    try:
        session_id, original_filename = key.split('/', 1)
    except ValueError:
        # This handles cases where the key doesn't have a session prefix, like the root folder itself.
        print(f"Skipping key without session prefix: {key}")
        return

    # Ignore triggers from within a thumbnails folder to prevent infinite loops
    if 'thumbnails/' in original_filename:
        return
        
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        image_bytes = response['Body'].read()
        img = Image.open(io.BytesIO(image_bytes))
        
        basic_metadata = {
            'format': img.format or 'JPEG',
            'size': f"{img.width}x{img.height}",
            'mode': img.mode
        }
        enhanced_metadata = get_exif_data(img)

        # Write metadata to DynamoDB using the full, original key
        table.put_item(
            Item={
                'ImageKey': key, # Partition key is now "session_id/filename.jpg"
                'BasicMetadata': basic_metadata,
                'EnhancedMetadata': enhanced_metadata
            }
        )

        # Create thumbnail
        size = (128, 128)
        img.thumbnail(size)
        
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')
        buffer.seek(0)
        
        # --- NEW: Construct the session-aware thumbnail key ---
        thumbnail_key = f"{session_id}/thumbnails/thumb-{original_filename}"
        
        s3_client.put_object(
            Bucket=bucket,
            Key=thumbnail_key,
            Body=buffer,
            ContentType='image/jpeg'
        )
        
        return {'status': 'success', 'key': thumbnail_key}
        
    except Exception as e:
        print(f"Error processing image {key}: {e}")
        raise e