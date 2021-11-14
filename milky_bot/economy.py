import discord
import random
from replit import db

def pretty_nickname(auth):
  pretty_nick = "٩(˘◡˘)۶ {} ᕙ(`▿´)ᕗ".format(auth)
  return pretty_nick

def set_balance(message, balance = 0):
  str_auth_id = message.author.id
  if str_auth_id not in db.keys():
    db[str_auth_id] = {"bal":balance}
  balset = ("balance set to {}".format(balance))
  return balset

def get_balance(message):
  str_auth_id = str(message.author.id)
  #if auth_id in db.keys():
  bal = db[str_auth_id]["bal"]
  return bal
  """else:
    set_balance(str_auth_id)
    bal = db[str_auth_id]["bal"]
    return bal
"""

#updates the user's balance given the value
def update_balance(message, value):
  str_auth_id = str(message.author.id)
  db[str_auth_id]["bal"] += value
  bal = db[str_auth_id]["bal"]
  return bal

#50% chance for the player to gain or lose a random amount of money, ranging from 10 to 100 dollars.
def gamble(message, value):
  nickname = message.author.display_name
  bet = int(value)
  if get_balance(message) > bet:
    update_balance(message, -bet)
    if random.randint(1,2) == 1:
      loss = bet * (0-random.randint(1,10))
      update_balance(message, bet * loss)
      curbal = get_balance(message)
      return (f"{nickname} gambled and lost {loss} dollars! Current Balance: {curbal}")
    else:
      gain = bet * (random.randint(1,10))
      update_balance(message, gain)
      curbal = get_balance(message)
      return (f"{nickname} gambled and gained {gain} dollars! Current Balance: {curbal}")
  elif get_balance(message) >= 0 and get_balance(message) < bet:
    return "You don't have enough money to gamble!"
  else:
    return "You can't gamble with a debt! Work to gain money!"