import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('photo_subject')
    result = table.query(
        ProjectionExpression='file_key',
        KeyConditionExpression=Key('subject').eq(event['subject'])
    )
    return result['Items']
