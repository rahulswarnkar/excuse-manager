from dynamodb_json import json_util as dynamodb_json
from functools import reduce
from uuid import uuid4
import json
import boto3

table_name = 'excuse-manager-dev-em'
client = boto3.client('dynamodb', region_name='eu-west-1')

def add(event, context):
    print(event)
    print(context)
    body = json.loads(event['body'])
    if 'message' not in body:
        raise Exception('No message found')
    item = {
        'type': 'excuse',
        'id': str(uuid4()),
        'author': deep_get(event, 'requestContext', 'identity', 'sourceIp'),
        'message': body['message']
    }
    print('Adding', item)
    client.put_item(TableName=table_name, Item=json.loads(dynamodb_json.dumps(item)))
    return {
        "statusCode": 201
    }

def list(event, context):
    print(event)
    print(context)
    limit = deep_get(event, 'queryStringParameters', 'limit')
    last = deep_get(event, 'queryStringParameters', 'last')
    sort = deep_get(event, 'queryStringParameters', 'sort')

    query_result = client.query(TableName = table_name,
        KeyConditionExpression = '#key = :value',
        ExpressionAttributeNames = {
            '#key' : 'type'
        },
        ExpressionAttributeValues = {
            ':value' : {
                'S' : 'excuse'
            }
        }
    )
    print(query_result)

    parsed_result = dynamodb_json.loads(query_result)
    print(parsed_result)
    result = {
        "last": deep_get(parsed_result, 'LastEvaluatedKey', 'id'),
        "size": parsed_result['Count'],
        "items": parsed_result['Items']
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }

def deep_get(dictionary, *keys):
    return reduce(lambda d, key: d.get(key, None) if isinstance(d, dict) else None, keys, dictionary)
