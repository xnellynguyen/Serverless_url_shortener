import json
import boto3

def lambda_handler(event, context):
    #initialize dynamoDB
    dynamodb = boto3.resource('dynamodb')
    urls_table = dynamodb.Table('URLs')

    #get short url from path
    short_url = event['pathParameters']['shortUrl']

    #retreive original url
    response = urls_table.get_item(Key={'shortUrl': short_url})
    original_url = response['Item']['originalUrl']

    #redirect to og url
    return {
        'statusCode': 302,
        'headers': {'Location': original_url},
        'body': json.dumps({'message': 'Redirecting...'})
    }