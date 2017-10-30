#! /usr/local/bin/Python3.5

import boto3

s3 = boto3.Session(profile_name="<profile>").client("s3")

s3.put_object(
    Bucket='rekognitiondataset',
    Body='~/Images/ProfilePhotos02.jpg',
    Key='ProfilePhotos02.jpg'
)
