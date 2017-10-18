#! /usr/local/bin/Python3.5

import boto3

polly = boto3.Session(profile_name="gekko1").client('polly')

response = polly.synthesize_speech(
    OutputFormat='mp3',
    SampleRate='8000',
    Text='Salut, je m\'appelle Benjamin',
    TextType='text',
    VoiceId='Mathieu'
)

# print(type(response['AudioStream'].read()))

with open("test", 'wb') as file:
    file.write(response['AudioStream'].read())
