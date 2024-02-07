import json

with open('products.txt', 'r') as f:
    data = json.load(f)
print(data)

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
 #       'body': json.dumps('Again This is the next change I am going GetProductList Lambda....!')
        'body' : json.dumps(data)
    }
