import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from code import *


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    number=request.values.get('From')
    
    outging_sms(number,body)
    return ""

def outging_sms(number,body):
    account_sid = 'AC4464f1edbc6a2294a3594298f1a25d4d'
    auth_token = 'b6ff1d80e3e98e04db43ce5174374f18'
    client = Client(account_sid, auth_token)
    return_message=body+" is your response that has been recieved. Kindly wait for futher details. " + str(number)
    message = client.messages \
                    .create(
                        body=return_message,
                        from_='+19497494849',
                        to=number
                    )
    print(message.sid)

if __name__ == "__main__":
    app.run(debug=True)