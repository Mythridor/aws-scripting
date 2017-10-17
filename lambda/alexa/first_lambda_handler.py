def build_response(session_attributes, speech_response):
    return {
        'version': 1.0,
        'session_attributes': session_attributes,
        'response': speech_response
    }


def build_speech_response(title, output, reprompt_text, ending_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeech <> " + title,
            'content': "SessionSpeech <> " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        "shouldEndSession": ending_session
    }


def get_launching_speech():
    # Called to tell Alexa to say something
    return build_response({}, build_speech_response("Test", "This is a Test", "Can you repeat please ?", False))


def on_session_started(session_started_request, session):
    # Called at the beginning of the Session
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch():
    return get_launching_speech()


def lambda_handler(event, context):
    print(event)
    print(context)

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
