import requests
import json

class TokenUnauthorised(Exception):
  def __init__(self, *args: object) -> None:
      super().__init__(*args)

class TokenNotFound(Exception):
  def __init__(self, *args: object) -> None:
      super().__init__(*args)

class ChannelNotFound(Exception):
  def __init__(self, *args: object) -> None:
      super().__init__(*args)


def get_profile(token: str):
  headers = {
    'authorization': token
  }
  
  account_id = requests.get("https://discordapp.com/api/users/@me", headers=headers)
  account = json.loads(account_id.text)
  if account_id.status_code == 401:
    raise TokenNotFound(f"Token \"{token}\" is not authorised, please make sure that \"{token}\" is a real discord acoount")
  if account_id.status_code == 404:
    raise TokenNotFound(f"Token \"{token}\" has no assoiciated profile.")
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
  if r.status_code == 401:
    raise TokenUnauthorised(f"Token \"{token}\" is not authorised to send a message to the channel {channel_id}. Please check the account's permission's or the channel id and try again.")
  if r.status_code == 404:
    raise ChannelNotFound(f"We could not find the channel {channel_id}.")

def get_messages(channel_id: int, token: str):
  header = {
    'authorization': token
  }
  message_log_request = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50', headers=header)
  message_log = json.loads(message_log_request.text)
  if message_log_request.status_code == 401:
    raise TokenUnauthorised(f"Token \"{token}\" is not authorised to send a message to the channel {channel_id}. Please check the account's permission's or the channel idand try again.")
  if message_log_request.status_code == 404:
    raise ChannelNotFound(f"We could not find the channel {channel_id}.")
  else:      
    return message_log

def get_latest_message(channel_id: int, token: str):
  header = {
    'authorization': token
  }
  message_log = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages?limit=50', headers=header)
  message_log_parsed = json.loads(message_log.text)
  if message_log.status_code == 401:
    raise TokenUnauthorised(f"Token \"{token}\" is not authorised to get messages from channel {channel_id}. Please check the account's permission's  or the channel id and try again.")
  if message_log.status_code == 404:
    raise TokenNotFound(f"Could not find the latest message for \"{token}\"")
  else:     
    return message_log_parsed[0]

def get_relatives(token: str):
  header = {
    'authorization': token
  }
  
  relatives = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=header)
  if relatives.status_code == 401:
    raise TokenUnauthorised(f"Token \"{token}\" is not authorised to view relatives. Please make sure that \"{token}\" is a real discord account")
  if relatives.status_code == 404:
    raise TokenUnauthorised(f"Could not find the relatives for \"{token}\"")
  relatives_parsed = json.loads(relatives.text)
