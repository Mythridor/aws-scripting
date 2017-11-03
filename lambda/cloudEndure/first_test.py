#! /usr/local/bin/Python3.5

import requests
import json
import sys

API_ENTRY_POINT = 'https://console.cloudendure.com/api/latest/'
HEADERS = {'Content-Type': 'application/json'}


id = {'username': '<username>', 'password': '<password>'}
request = requests.post(API_ENTRY_POINT + 'login', data=json.dumps(id), headers=HEADERS)
print(request.text)

session = {'session': request.cookies["session"]}

project_list = requests.get('https://console.cloudendure.com/api/latest/projects', headers=HEADERS, cookies=session)

print(project_list.text)

#project_id = json.loads(project_list.text)["Items"][0]["id"]

#print(project_id)

create_project = requests.post(API_ENTRY_POINT + 'projects')

print(create_project.text)