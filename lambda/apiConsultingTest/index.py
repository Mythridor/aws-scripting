import requests

def lambda_handler(event, context):
    response = requests.get("http://api.open-notify.org/astros.json")
    print response
