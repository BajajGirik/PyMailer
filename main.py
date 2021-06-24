from email.message import Message
import smtplib
import os
from dotenv import load_dotenv

# loads environment variables from .env file
load_dotenv()

Sender_Email = os.getenv('EMAIL_ADDRESS')
Password = os.getenv('EMAIL_PASSWORD')

PORT = 25

# taking mailing details from user
print("Enter Mail details:")
Receiver_Email = input("TO: ")
Subject = input("SUBJECT: ")
Body = input("BODY: ")
Message = f'Subject: {Subject}\n\n{Body}'

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