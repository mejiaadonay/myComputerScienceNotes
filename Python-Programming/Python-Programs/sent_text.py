from twilio import rest

# Sent MSN
# Author: Jose Escobar Mejia
# Date:   1/22/2016
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC115149ed615980cdb9ac130cd854855a"
auth_token  = "c13a53097d893bb1021e156f52cc955f"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Gricelda! I love you <3",
    to="+12025006492",    # Replace with your phone number
    from_="+14155992671") # Replace with your Twilio number
print message.sid
