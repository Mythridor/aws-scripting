import boto3


def lambda_handler(event, context):
    print(event)
    client = boto3.client('rekognition')
    dynamodb = boto3.client('dynamodb')
    sns = boto3.client('sns')
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': event['Records'][0]['s3']['bucket']['name'],
                'Name': event['Records'][0]['s3']['object']['key']
            }}
    )

    print(response)
    for label in response['Labels']:
        if label['Confidence'] > 90:
            insert = dynamodb.put_item(
                TableName="<DBName>",
                Item={
                    'subject': {
                        'S': label['Name'],
                    },
                    'file_key': {
                        'S': event['Records'][0]['s3']['object']['key']
                    }
                }
            )

    if response['Labels'][1]["Name"] == "Person":
        response3 = client.compare_faces(
            SourceImage={
                'S3Object': {
                    'Bucket': event['Records'][0]['s3']['bucket']['name'],
                    'Name': event['Records'][0]['s3']['object']['key']
                }},
            TargetImage={
                'S3Object': {
                    'Bucket': '<ComparatingFileLocation>',
                    'Name': '<ComparatorFile>'
                }})
        print(response3)
        print(response3['FaceMatches'][0]['Similarity'])
        if response3['FaceMatches'][0]['Similarity'] >= 90:
            print("test")
            result = sns.publish(
                PhoneNumber='<PhoneNumber>',
                Message='Alerte! Un suspect a été identifié!',
                Subject='Warning',
            )
            print(result)
        print("Lambda executée")
