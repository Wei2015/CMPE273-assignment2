import boto3

def lambda_handler(event, context):
 
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('menu')
    
    attributes = event.keys()

    for k in attributes:
        if k!= 'menu_id':
            table.update_item(
                Key={
                    'menu_id':event['menu_id']
                },

                UpdateExpression= 'set ' + str(k) + '= :s',
                ExpressionAttributeValues={ 
                            ':s' : event[k]
            }
        )
