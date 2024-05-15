import json
import boto3

def lambda_handler(event, context):
    #initialize dynamoDB
    dynamodb = boto3.resource('dynamodb')
    urls_table = dynamodb.Table('URLs')

    #get short url from path with error handling
    if 'pathParameters' not in event or 'shortUrl' not in event['pathParameters']:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing short URL parameter'})
        }

    short_url = event['pathParameters']['shortUrl']

    #retreive original url
    response = table.get_item(Key={'shortUrl': short_url})

    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Short URL not found'})
        }

    original_url = response['Item']['originalUrl']

    #redirect to og url
    return {
        'statusCode': 302,
        'headers': {'Location': original_url},
        'body': json.dumps({'message': 'Redirecting...'})
    }