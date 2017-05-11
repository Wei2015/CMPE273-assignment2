import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    order_table = dynamodb.Table(event['TableName'])

    response = order_table.get_item(Key={'order_id':event['order_id']})
    order_info = response['Item']
    content = order_info['order_content']
    order_status = order_info['order_status']
    selection = content['selection']
    size = content['size']
    index = int(event['input'])-1
    
    if order_status == "selection":
        order_table.update_item(
            Key={
                'order_id':event['order_id']
            },
            UpdateExpression="set order_content.selection =:s, order_status =:r",
            ExpressionAttributeValues={':s': selection[index],
                                        ':r':"size"
                                    } 
        )
        size = "";
        index = 1;
        for k in content['size']:
            size += str(index) + "."
            size += k + " "
            index += 1
        sizeOption = {"Message": "Which size do you want? " + size}
        return sizeOption
        
    elif order_status == "size":
        order_table.update_item(
            Key={
                'order_id':event['order_id']
            },
            UpdateExpression="set order_content.size =:s, order_status =:r",
            ExpressionAttributeValues={':s': size[index],
                                        ':r':"processing"
                                        } 
        )
        table_menu = dynamodb.Table('menu')
        menu_info = table_menu.get_item(Key={'menu_id':order_info['menu_id']})
        menu_content = menu_info['Item']
        prices = menu_content['price']
        cost = prices[index]
        costMessage = {"Message":"Your order costs " + cost + ". We will email you when the order is ready. Thank you!"}
        
        order_table.update_item(
            Key={
                'order_id':event['order_id']
            },
            UpdateExpression="set order_content.cost = :c",
            ExpressionAttributeValues={':c': cost}
        )
        return costMessage