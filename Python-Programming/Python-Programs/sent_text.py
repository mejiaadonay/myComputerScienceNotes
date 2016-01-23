from twilio.rest import TwilioRestClient

# Sent MSN
# Author: Jose Escobar Mejia
# Date:   1/22/2016
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC115149ed615980cdb9ac130cd854855a"
auth_token  = "c13a53097d893bb1021e156f52cc955f"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+14159352345",    # Replace with your phone number
    from_="+14158141829") # Replace with your Twilio number
print message.sid
