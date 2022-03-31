from colorama import Fore
import requests
settings = [
  "Add token", 
  "Remove token", 
  "List all tokens",
  "Send message",
]

def printf(colour, message):
  exec(f"print(Fore.{colour} + \"{message}\" + Fore.RESET)")
  
class navigation:
  def __init__(self) -> None:
    self.choice = False

  def get_by_choice(self, options):
    for option in options:
      printf("BLUE", f"{options.index(option) + 1} | {option}")

    confirmation = input(Fore.YELLOW + "Please Select An Option > " + Fore.RESET)

    try:
      if options[int(confirmation)]:
        self.choice = int(confirmation)
        return int(confirmation)

    except ValueError:
      printf("RED", "Either you didnt say a number or I'm just an idiot")

    except IndexError:
      printf("RED", "Look at the fucking menu")
  

      
class alt:
  def __init__(self, token):
    self.tokens = [
      token
    ]
    printf("GREEN", f"Set new token {token}")
  
  def add_token(self, new_token):
    self.tokens.append(new_token)
    printf("GREEN", f"Set new token {new_token}")
  
  def remove_token(self, id: int):
    self.tokens.remove(self.tokens[id])
    printf("GREEN", "Token removed")

  def send_message(self, message, link):
    if not self.tokens:
      printf("RED", "How do you think imma send a message without a goddamn token")

default_token = input("Before you continue, please type in a token for use > ")
alt_manager = alt(default_token)
while True:
  interpret = navigation()
  interpret.get_by_choice(settings)
  if interpret.choice:
    if interpret.choice == 1:
      get_token = input("Please enter a token > ")
      alt_manager.add_token(get_token)
    elif interpret.choice == 2:
      get_id = input("Please enter the ID of the token, you can find the ID of a token with option No. 3 in the main menu > ")
      try:
        alt_manager.remove_token(int(get_id))
      except IndexError:
        printf("RED", "Mmmm that ID doesn't exist")
      except ValueError:
        printf("RED", "What the fuck you on about")

    elif interpret.choice == 3:
      for token in alt_manager.tokens:
        printf("BLUE", f"\\nID: {alt_manager.tokens.index(token)} | Token: {token}\\n")

  