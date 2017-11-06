#! /usr/local/bin/Python3.5

import datetime
import json
import random
import time

import boto3

highHeartrateNames = ['Bailey', 'Beatrice', 'Beau', 'Bella', 'Ben', 'Beth']
nonhighHeartrateNames = ['Branden', 'Brady', 'Bonny']

allNames = list(set().union(highHeartrateNames, nonhighHeartrateNames))

iot = boto3.Session(profile_name="gekko1").client('iot-data')


# generate normal heart rate with probability .95
def getNormalHeartRate():
    data = dict()
    data['heartRate'] = random.randint(60, 100)
    data['rateType'] = 'NORMAL'
    data['userId'] = random.choice(allNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (data)


# generate high heart rate with probability .05 (very few)
def getHighHeartRate():
    data = dict()
    data['heartRate'] = random.randint(150, 200)
    data['rateType'] = 'HIGH'
    data['userId'] = random.choice(highHeartrateNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (data)


while True:
    time.sleep(1)
    rnd = random.random()
    data = ''
    if rnd < 0.05:
        data = json.dumps(getHighHeartRate())
    else:
        data = json.dumps(getNormalHeartRate())

    print(data)
    response = iot.publish(
        topic='/health/heartrate',
        payload=data
    )
