import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from code3 import *
from mail import *


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    number=request.values.get('From')
    
    outging_sms(number,flagship_department(body),body)
    return ""

def outging_sms(number,department,body):
    account_sid = 'AC3edc22200ecf6413ddb792ba3e9d878d'
    auth_token = '131ce5e911472ea66e78a0a7c7e0d9d3'
    client = Client(account_sid, auth_token)

    return_message="Your response that has been sent to "+department+". Kindly wait for futher details. "
    message = client.messages \
                    .create(
                        body=return_message,
                        from_='+19403985871',
                        to=number
                    )
    print(message.sid)
    mail_to_department(department,number,body)

if __name__ == "__main__":
    app.run(debug=True)