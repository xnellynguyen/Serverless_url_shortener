import json
import boto3

def lambda_handler(event, context):
    # Initialize DynamoDB
    dynamodb = boto3.resource('dynamodb')
    urls_table = dynamodb.Table('URLs')

    # Get short URL from query string parameter
    try:
        short_url = event['queryStringParameters']['url']
    except KeyError:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Missing URL parameter'})
        }

    # Retrieve original URL
    response = urls_table.get_item(Key={'shortUrl': short_url})
    if 'Item' not in response:
        return {
            'statusCode': 404,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Short URL not found'})
        }

    original_url = response['Item']['originalUrl']

    # Redirect to the original URL
    return {
        'statusCode': 302,
        'headers': {
            'Location': original_url
        },
        'body': json.dumps({'message': 'Redirecting...'})
    }
