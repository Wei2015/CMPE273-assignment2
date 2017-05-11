import boto3
import json


def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('menu')
    response = table.get_item(
           Key={
               'menu_id':event['menu_id']
           }
    )
    return response['Item']
        
