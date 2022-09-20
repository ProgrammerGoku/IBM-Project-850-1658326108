#Done by Gokul Ram(2019504521)

import random
import smtplib
from email.message import EmailMessage

thresh=36.5
'''#An optional mail sending function to alert using mail
def send_mail():
  send_add="gokul.subramani33@gmail.com"
  to_add="kgurubaran2006@gmail.com"
  passw='coqoekeamuuckapc'
  s=smtplib.SMTP_SSL("smtp.gmail.com",port=465)
  s.login(send_add,passw)
  msg=EmailMessage()
  msg.set_content("Alert!High temperature detected!!")
  msg['From']="gokul.subramani33@gmail.com"
  msg['To']="Concened_auth@gmail.com"

  s.sendmail(send_add,to_add,msg.as_string())
  s.quit()

'''
  
while(True):
  print("****READING HUMIDITY AND TEMPERATURE VALUE****")
  (temp,humidity)=(random.uniform(30,45),random.uniform(30,50))
  print("Temperature value is{0:0.1f} Humidity is {1:0.1f}%\n".format(temp,humidity))
  if(temp>thresh):
    #send_mail()
    print("***ALERT!!Temperature has exceeded the range***\n")
