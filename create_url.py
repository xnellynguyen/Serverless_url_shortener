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
    #store in dynamoDB
    #return shortened url