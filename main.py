import os
import json
from credentials import client , TWILIO_NUMBER
from dotenv import load_dotenv
from data import api_data
import time

load_dotenv()
File_path = "match-ids.json"


class ErrorSendingMessage(Exception):
     pass


def load_matches():
 if not os.path.exists(File_path):
     return {}
 with open(File_path,"r") as file:
     data = json.load(file)
     if data:
        return data
     else:
        return {}


def save_data(match_id,date):
  data = load_matches()
  with open(File_path,"w") as file:
    data[match_id] = {
       "alert":True,
       "date":date
    }
    json.dump(data,file,indent=2)
      
   

def send_alert(message:str):
  if message:
     client.messages.create(
          body=message,
          from_=TWILIO_NUMBER,
          to="whatsapp:+923152471268"
     )
  else:
     raise ErrorSendingMessage("Error sending message!")


def polling(): 
  while True:
    try:
      response,match_id,status,date =  api_data()
      matches_alerts = load_matches()
      if status and match_id not in matches_alerts:
        send_alert(response)
        save_data(match_id,date)
        print("alert sent!")
      else:
        print("match not started!")
    except ErrorSendingMessage as e:
      print(e)
    time.sleep(15*60*60)
   
polling()
       