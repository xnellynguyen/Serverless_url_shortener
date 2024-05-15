import json
import boto3
import hashlib

def lambda_handler(event, context):
    print("Received event:", event)  # Log the entire event to see what is received
    
    # Initialize DynamoDB
    dynamo_db = boto3.resource('dynamodb')
    urls_table = dynamo_db.Table('URLs')

    # Get URL from query string
    try:
        original_url = event['queryStringParameters']['url']
    except TypeError:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'No URL provided'})
        }

    # Create shortened URL
    sha256_hash = hashlib.sha256(original_url.encode()).hexdigest()[:8]

    # Store in DynamoDB with error handling
    try:
        urls_table.put_item(Item={'shortUrl': sha256_hash, 'originalUrl': original_url})
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }

    # Return shortened URL
    return {
        'statusCode': 200,
        'headers': {'Access-Control-Allow-Origin': '*'},
        'body': json.dumps({'shortUrl': sha256_hash})
    }
