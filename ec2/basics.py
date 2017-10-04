#! /usr/local/bin/python3.5

import boto3
import time

def list_all_ec2():
    ec2 = boto3.resource('ec2')
    return ec2.instances.all()


def create_instance():
    ec2 = boto3.resource('ec2')

    instance = ec2.create_instances(
        ImageId='ami-ebd02392',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='Mythri',
        NetworkInterfaces=[{
            'DeviceIndex': 0,
            'SubnetId': 'subnet-35debb52',
            'AssociatePublicIpAddress': True,
            'Groups': ['sg-a73667df']
        }]
    )
    while instance[len(instance) - 1].state == "pending":
        print(instance, instance.state)
        time.sleep(5)
        instance.update()

        instance.add_tag("Name", "test")

    print("done", instance)


def terminate_all_ec2():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        instance.terminate()


def stop_all_ec2():
    ec2 = boto3.resource('ec2')
    for instance in ec2.instances.all():
        instance.stop()

[print(x) for x in list_all_ec2()]