#######CODE ALONG WITH VIDEO

from art import logo, vs
from game_data import data
import random
from replit import clear



def format_data(account):
  """Format account data into printable format."""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc} from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follow counts and returns if they got it right"""
  if a_followers > b_followers:
    if guess == "a":
      return guess == "a" #this will evaluate this statement and return a True or False
    else:
      return guess == "b"


#Display Art
print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)

#Make game repeatable
while game_should_continue:
  #Making the account at position b becoming the next position a


  #Generate random accounts from game data
  account_a = account_b
  account_b = random.choice(data)
  
  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  # print(vs)
  print(f"Compare B: {format_data(account_b)}")

  #Ask user for a guess.
  guess = input("Who as more followers? Type 'A' or 'B'.").lower()

  #Check is user is correct.
  ##Get Follower accounts of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  #Clear the screen between rounds
  clear()
  print(logo)
  #Give user feedback on their guess
  #Score Keeping
  if is_correct: ##meaning, if it is True
    score += 1
    print("You're right!")
  else:
    game_should_continue = False
    print(f"Nope sorry. Final score: {score}")
    
  