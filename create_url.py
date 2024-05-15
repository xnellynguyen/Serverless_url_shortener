import json
import boto3
import hashlib

def generate_short_url(event, context):
    #initialize dynamoDB
    dynamo_db = boto3.resource('dynamodb')
    urls_table = dynamo_db.Table('URLs')

    #get url from query string
    original_url = event['queryStringParameters']['url']

    #create shortened url
    sha256_hash = hashlib.sha256(original_url.encode()).hexdigest()[:8]  
    
    #store in dynamoDB
    #return shortened url