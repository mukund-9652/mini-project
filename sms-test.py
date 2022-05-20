# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC4464f1edbc6a2294a3594298f1a25d4d'
auth_token = '66696f67b3ce6d7a57b76a5ce9a3ea34'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Your response has been recieved. Kindly wait for futher details.",
                     from_='+19497494849',
                     to='+917845159519'
                 )

print(message.sid)
