from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID=os.getenv("ACCOUNT_SID")
AUTH_TOKEN=os.getenv("AUTH_TOKEN")
TWILIO_NUMBER=os.getenv("TWILIO_NUMBER")

client = Client(ACCOUNT_SID,AUTH_TOKEN)