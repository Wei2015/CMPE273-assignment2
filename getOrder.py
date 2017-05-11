import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(event['TableName'])
    response = table.get_item(
           Key={
               'order_id':event['order_id']
           }
    )
    return response['Item']