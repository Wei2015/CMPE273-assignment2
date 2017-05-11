import boto3

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    orderTable = dynamodb.Table('order')
    table.update_item(
        Key={'order_id': event['order_id']},
        UpdateExpression: "ADD a
