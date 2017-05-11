import boto3
import time
from time import strftime

def handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    #retrieve menu info
    table = dynamodb.Table('menu')
    response = table.get_item(
           Key={
               'menu_id':event['menu_id']
           }
    )
    menu = response['Item']
    customer_name = event['customer_name']
    selection = "";
    index = 1;
    for k in menu['selection']:
        selection += str(index) + "."
        selection += k + " "
        index += 1

    greeting = {"Message": "Hi " + customer_name + ", please choose one of these selections:"+ selection}

    current_time = strftime("%m-%d-%Y@%H:%M:%S", time.localtime())
    orderTable = dynamodb.Table('order')
    orderTable.put_item(
        Item={
               'menu_id':event['menu_id'],
               'order_id':event['order_id'],
               'customer_name': event['customer_name'],
               'customer_email':event['customer_email'],
               'order_status': 'selection',
               'order_content': {
                   'selection': menu['selection'],
                   'size':menu['size'],
                   'cost':"0.0",
                   'order_time': current_time
                }
           }
        )
    return greeting
