import smtplib
import os
from dotenv import load_dotenv

# loads environment variables from .env file
load_dotenv()

Sender_Email = os.getenv('EMAIL_ADDRESS')
Password = os.getenv('EMAIL_PASSWORD')

PORT = 8000
# setting up server at port: 8000
