from random import randint
import smtplib
limit= 35
mail_id=input("Enter sender Mailid")
password=input("Enter sender password")
receiver=input("Enter receiver Mailid")
def mail():
    connect=smtplib.SMTP('smtp.gmail.com',587)
    connect.starttls()
    connect.login(mail_id,password)
    connect.sendmail(mail_id,receiver,'Alert!')
    print("Mail sent")
while(True):
    temperature,humidity=randint(25,40),randint(25,40)
    if temperature>limit:
        print("Alert! high temperature")
        mail()       
    if humidity>limit:
        print("Humidity level=",humidity)
        mail()
