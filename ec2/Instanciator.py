from boto3 import Session


class ec2Instanciator:
    instance_id = 0

    def __init__(self, ami, instance_type, key_name, subnet_id, profile_name="", groups=list()):
        self.ec2 = Session(profile_name=profile_name).resource('ec2')
        self.ami = ami
        self.instance_type = instance_type
        self.key_name = key_name
        self.subnet_id = subnet_id
        if type(groups) == 'list':
            self.groups = groups  # Must be a list
        ec2Instanciator.instance_id += 1
        self.instance_id = ec2Instanciator.instance_id

    def get_id(self):
        return self.instance_id

    def create(self):
        self.ec2.create_instances(
            ImageId=self.ami,
            MinCount=1,
            MaxCount=1,
            InstanceType=self.instance_type,
            KeyName=self.key_name,
            NetworkInterfaces=[{
                'DeviceIndex': 0,
                'SubnetId': self.subnet_id,
                'AssociatePublicIpAddress': True,
                'Groups': self.groups
            }]
        )

    def stop(self):
        self.ec2.instances.filter(InstanceIds=self.get_id()).stop()

    def terminate(self):
        self.ec2.instances.filter(InstanceIds=self.get_id()).terminate()
