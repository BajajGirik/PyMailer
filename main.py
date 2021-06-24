import smtplib
import os
from dotenv import load_dotenv
import re

# loads environment variables from .env file
load_dotenv()

Sender_Email = os.getenv('EMAIL_ADDRESS')
Password = os.getenv('EMAIL_PASSWORD')

PORT = 25

# for validating an email that user enters 
Emailregex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

# taking mailing details from user
print("Enter Mail details:")
Receiver_Email = input("TO: ") or 'bajajgirik2010@gmail.com'
Subject = input("SUBJECT: ") or 'Test Mail'
Body = input("BODY: ") or 'Hello World!'
Message = f'Subject: {Subject}\n\n{Body}'

if re.search(Emailregex, Receiver_Email):
    try:
        # setting up server at port: 8000
        server = smtplib.SMTP('smtp.gmail.com', PORT)

        server.ehlo()
        # connection in "Transport Layer Security" mode
        server.starttls()
        server.ehlo()

        # Login with the account you want to send mail from and send the msg
        server.login(Sender_Email, Password)
        server.sendmail(Sender_Email, Receiver_Email, Message)

        # ending the session 
        print("Mail Sent")

    except: 
        print("Unsuccessful")

    finally:
        server.quit()

else:
    print("Please enter a valid email")       