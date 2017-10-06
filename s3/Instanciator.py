from boto3 import Session, client


class s3Instanciator:
    def __init__(self, profile, name):
        self.client = client('s3')
        self.profile = profile
        self.s3 = Session(profile_name=self.profile).client('s3')
        self.name = name

    def create(self):
        self.s3.create_bucket(
            Bucket=self.name,
            CreateBucketConfiguration={'LocationConstraint': Session(profile_name=self.profile).region_name}
        )
