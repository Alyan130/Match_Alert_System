import requests
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("CRIKCET_API_KEY")


def api_data(): 
  res = requests.get(f"https://api.cricapi.com/v1/matches?apikey={KEY}&offset=0")
  data = res.json()
  matches = data["data"]
  latest = matches[0]
  teams = latest["teams"]
  team1 = teams[0]
  team2 = teams[1]
  venue = latest["venue"]
  match_type = latest["matchType"]

  status = latest['matchStarted']  
  date = latest['date']
  match_id = latest['id']

  reponse = f"The {match_type} match has started between {team1} and {team2} at {venue}."
  return reponse,match_id,status,date 


  
  