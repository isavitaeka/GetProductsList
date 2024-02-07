import json

with open('products.txt', 'r') as f:
    data = json.load(f)
print(data)

def lambda_handler(event, context):
    # TODO implement
    return {
        "isBase64Encoded": "false",
        'statusCode': 200,
        "headers": {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,PUT',
        'Content-Type': 'application/json'


        },
 #       'body': json.dumps('Again This is the next change I am going GetProductList Lambda....!')
        'body' : json.dumps(data)
    }
