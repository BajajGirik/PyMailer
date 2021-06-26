import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import utils

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
print("Enter the file name you want to attach in mail")
Attachment = input("(Press Enter to skip): ")

if utils.checkEmail(Receiver_Email):
    try:
        # setting up server at port: 25
        server = smtplib.SMTP('smtp.gmail.com', PORT)

        server.ehlo()
        # connection in "Transport Layer Security" mode
        server.starttls()
        server.ehlo()

        # Login with the account you want to send mail from and send the msg
        server.login(Sender_Email, Password)

        # creating msg to be sent 
        msg = EmailMessage()

        msg['Subject'] = Subject
        msg['From'] = Sender_Email
        msg['To'] = Receiver_Email
        msg.set_content(Body)
      
        # sending the message on gmail 
        server.send_message(msg)

        print("Mail Sent")

    except: 
        print("Unsuccessful")

    finally:
        # ending the session 
        server.quit()

else:
    print("Please enter a valid email")       