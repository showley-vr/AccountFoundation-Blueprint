import json
import boto3

def handler(event, context):
    
    iam = boto3.resource('iam')
    response = iam.create_user(UserName="test-boto3-user")
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }