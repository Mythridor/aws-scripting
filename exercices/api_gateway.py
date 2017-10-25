#! /usr/local/bin/Python3.5

import json

import requests

data = {"device_name": "deviceTest"}

response = requests.put("https://rkh83nul54.execute-api.eu-west-1.amazonaws.com/beta/devices", data=json.dumps(data))

test = json.loads(response.content.decode('utf-8'))
print("Device " + test['devicename'] + " (" + test['deviceid'] + ") created.")

userData = {"user_name": "userTest"}

responseUser = requests.put("https://rkh83nul54.execute-api.eu-west-1.amazonaws.com/beta/users",
                            data=json.dumps(userData))

testUser = json.loads(responseUser.content.decode('utf-8'))
print("User " + testUser['username'] + " (" + testUser['userid'] + ") created.")

simcardData = {"simcard_name": "simcardTest"}

responseSimcard = requests.put("https://rkh83nul54.execute-api.eu-west-1.amazonaws.com/beta/simcards",
                               data=json.dumps(simcardData))

testSimcard = json.loads(responseSimcard.content.decode('utf-8'))
print("User " + testSimcard['simcardname'] + " (" + testSimcard['simcardid'] + ") created.")

responseSimcard = requests.post(
    "https://rkh83nul54.execute-api.eu-west-1.amazonaws.com/beta/devices/" + test['deviceid'] + "/simcards/" +
    testSimcard['simcardid'])

print("Association created.")
