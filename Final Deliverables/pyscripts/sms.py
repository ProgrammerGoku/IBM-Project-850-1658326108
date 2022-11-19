import os
from twilio.rest import Client 
 
account_sid = 'ACb4d033465895822c34e656bf6be69384' 
auth_token = '6916b3bf66a451937068378db5a9692a' 
client = Client(account_sid, auth_token) 
def send_sms():
    message = client.messages.create(  
                              messaging_service_sid='MG3d02a8b50e684c345993182610957703', 
                              body='Alert the water is not in good quality !',    
                              from_='+16294006922',  
                              to='+919442130329' 
                          ) 
 
    print(message.sid)