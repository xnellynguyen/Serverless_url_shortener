import json
import boto3

def lambda_handler(event, context):
    # Initialize DynamoDB
    dynamodb = boto3.resource('dynamodb')
    urls_table = dynamodb.Table('URLs')

    # Get short URL from path with error handling
    try:
        short_url = event['pathParameters']['shortUrl']
    except KeyError:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Missing short URL parameter'})
        }

    # Retrieve original URL
    try:
        response = urls_table.get_item(Key={'shortUrl': short_url})
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'Short URL not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }

    original_url = response['Item']['originalUrl']

    # Redirect to the original URL
    return {
        'statusCode': 302,
        'headers': {
            'Location': original_url,
            'Access-Control-Allow-Origin': '*'  # Optional here as it’s a redirect
        },
        'body': json.dumps({'message': 'Redirecting...'})
    }
