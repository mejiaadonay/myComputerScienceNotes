from twilio.rest import TwilioRestClient

# Sent MSN
# Author: Jose Escobar Mejia
# Date:   1/22/2016
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC32a3c49700934481addd5ce1659f04d2"
auth_token  = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+14159352345",    # Replace with your phone number
    from_="+14158141829") # Replace with your Twilio number
print message.sid
