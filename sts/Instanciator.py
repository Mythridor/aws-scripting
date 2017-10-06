from boto3 import client, Session


class stsInstanciator:
    def __init__(self, role_arn, role_session_name, profile):
        self.profile = profile
        self.role_arn = role_arn
        self.role_session_name = role_session_name
        self.ref = Session(profile_name=self.profile).client('sts').assume_role(
            RoleArn=role_arn,
            RoleSessionName=role_session_name
        )
        self.client = client(
            's3',
            aws_access_key_id=self.ref['Credentials']['AccessKeyId'],
            aws_secret_access_key=self.ref['Credentials']['SecretAccessKey'],
            aws_session_token=self.ref['Credentials']['SessionToken']
        )

    def put(self, bucket_name, file, key):
        self.client.put_object(
            Bucket=bucket_name,
            Body=file,
            Key=key
        )

    def create(self, name):
        self.client.create_bucket(
            ACL='public-read-write',
            Bucket=name,
            CreateBucketConfiguration={'LocationConstraint': Session(profile_name=self.profile).region_name}
        )
