
import boto3



def handler(event, context):
 
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('menu')

    table.put_item(
           Item={
               'menu_id':event['menu_id'],
               'store_name':event['store_name'],
               'selection':event['selection'],
               'size':event['size'],
               'price':event['price'],
               'store_hours':event['store_hours']
           }
    )
        
