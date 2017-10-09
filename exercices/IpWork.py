#! /usr/local/bin/python3.5
import time

import boto3
import requests


class ApiRequester:
    def __init__(self, url="", parameters={}):
        self.url = url
        self.parameters = parameters

    def consult(self):
        start = time.time()
        request = requests.get(self.url, params=self.parameters)
        print("{:.2f} ms".format((time.time() - start) * 1000))
        return request.json()


request = ApiRequester("https://api.ipify.org/", {"format": "json"}).consult()
ip_adress = request['ip']

print(ip_adress)

ec2 = boto3.Session(profile_name="gekko2", region_name='eu-west-1').client('ec2')

ec2.authorize_security_group_ingress(
    GroupId='sg-b95040c1',
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': ip_adress + '/32',
                    'Description': 'Test'
                }
            ],

            'ToPort': 22,
        },
    ],
)

ec2.revoke_security_group_ingress(
    CidrIp='0.0.0.0/0',
    GroupId='sg-b95040c1',
    IpProtocol='tcp',
    FromPort=22,
    ToPort=22
)