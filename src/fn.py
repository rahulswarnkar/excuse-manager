from dynamodb_json import json_util as dynamodb_json
import json
import boto3

client = boto3.client('dynamodb', region_name='eu-west-1')

def handler(event, context):
    print("Event:", event)
    print("Function name:", context.function_name)
    print("Function version:", context.function_version)
    print("Function ARN:", context.invoked_function_arn)
    print("AWS request id:", context.aws_request_id)
    print("Log stream name:", context.log_stream_name)
    print("Log group name:",  context.log_group_name)
    print("Request ID:",context.aws_request_id)
    print("Mem. limits(MB):", context.memory_limit_in_mb)

    key = {
        'type': 'excuse',
        'id': '20190922T220000-VFXOYYQA'
    }
    print('Key', json.loads(dynamodb_json.dumps(key)))
    response = client.get_item(TableName='excuse-manager-dev-em', Key=json.loads(dynamodb_json.dumps(key)))
    excuse = response['Item']
    print('Response', response, '\n')
    return {
        "statusCode": 200,
        "body": json.dumps(dynamodb_json.loads(excuse))
    }