import requests
import json


def get_profile(token: str):
  headers = {
    'authorization': token
  }
  
  account_id = requests.get("https://discordapp.com/api/users/@me", headers=headers)
  print(account_id.text)
  account = json.loads(account_id.text)
  if account == {'message': '401: Unauthorized', 'code': 0}:
    return 0
  else:
    return account

def send_message(message: str, channel_id: int, token: str):
  header = {
    'authorization': token
  }
  payload = {
    'content': message
  }
  r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=header, data=payload)

def get_messages(channel_id: int, token: str):
  header = {
    'authorization': token
  }
  message_log = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50', headers=header)
  message_log = json.loads(message_log.text)
  if message_log == {'message': '401: Unauthorized', 'code': 0}:
    return 0
  else:      
    return message_log


def get_latest_message(channel_id: int, token: str):
  header = {
    'authorization': token
  }
  message_log = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50', headers=header)
  message_log_parsed = json.loads(message_log.text)
  if message_log_parsed == {'message': '401: Unauthorized', 'code': 0}:
    return 0
  else:     
    return message_log_parsed[0]

def get_guilds(token: str):
  pass

def delete_message(message_id: int, channel_id: int, token: str):
  header = {
    'authorization': token
  }
  requests.delete("https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}", headers=header)