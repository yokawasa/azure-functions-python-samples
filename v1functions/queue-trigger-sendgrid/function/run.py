# -*- coding: utf-8 -*-
"""

Azure Functions Queue Trigger Python Sample that send email by using SendGrid bindings.

SendGrid binding reference:
https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-sendgrid
"""
import os, json

_AZURE_FUNCTION_QUEUE_INPUT_ENV_NAME = "inputMessage"
_AZURE_FUNCTION_SENDGRID_OUTPUT_ENV_NAME = "outputMessage"
_SENDGRID_EMAIL_TO = "receiver@contoso.com"
_SENDGRID_EMAIL_SUBJECT = "Mail Subject"

# read the queue message
messageText = open(os.environ[_AZURE_FUNCTION_QUEUE_INPUT_ENV_NAME]).read()
print("Function script processed queue message '{0}'".format(messageText))

outmsg={
    "personalizations": [
        { 
            "to": [{ "email": _SENDGRID_EMAIL_TO }]
        }
    ],
    "subject": _SENDGRID_EMAIL_SUBJECT,
    "content": [
        {
            "type": 'text/plain',
            "value": messageText
        }
    ]
 }

# Send email using SendGrid (output name: outputMessage)
print('Sending email using SendGrid:', outmsg)
with open(os.environ[_AZURE_FUNCTION_SENDGRID_OUTPUT_ENV_NAME], 'wb') as f:
    json.dump(outmsg,f)
