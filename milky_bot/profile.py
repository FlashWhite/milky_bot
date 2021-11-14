import discord
from discord import Color
from milky_bot.resources import bs
from replit import db

#throw error if color not provided
def hex_to_rgb(hex):
  return int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:], 16)

def welcome(message):
  msg_author = message.author
  str_auth_id = str(msg_author.id)
  db[str_auth_id] = {
    "bal":0, 
    "color":0, 
    "capybara_count":0, 
    "kudos":0
    }
  embed = discord.Embed(
      title="{}'s profile".format(msg_author.display_name),
      colour=db[str_auth_id]["color"],
      description="balance: {}".format(db[str_auth_id]["bal"])
    )
  embed.add_field(name="kudos:", value=db[str_auth_id]["kudos"], inline=True)
  embed.add_field(name="capybara count:", value=db[str_auth_id]["capybara_count"], inline=True)
  embed.set_author(name=msg_author, icon_url=msg_author.avatar_url)
  return embed

def init_user(message):
  str_auth_id = str(message.author.id)
  db[str_auth_id] = {
    "bal":0, 
    "color":0, 
    "capybara_count":0, 
    "kudos":0
    }
  return "profile created"

def display_profile(message):
  str_auth_id = str(message.author.id)
  bal = db[str_auth_id]["bal"]
  color = db[str_auth_id]["color"]
  capy_count = db[str_auth_id]["capybara_count"]
  kudos = db[str_auth_id]["kudos"]
  profile_stats = (f"balance: {bal}, color: {color}, capybara count: {capy_count}, kudos: {kudos}")
  return profile_stats


def start(message):
  msg_author = message.author
  str_auth_id = str(msg_author.id)
  values = message.content.lstrip(">").split()
  db[str_auth_id] = {"bal":0, "color":int(values[1]), "capybara_count":0, "kudos":0}
  return "added {} with balance {} and color {}".format(msg_author, db[str_auth_id]["bal"], db[str_auth_id]["color"])
  """
  if str_auth_id not in db.keys():
    db[str_auth_id] = {"bal":0, "color":int(values[1]), "capybara_count":0, "kudos":0}
    return "added {} with balance {} and color {}".format(msg_author, db[str_auth_id]["bal"], db[str_auth_id]["color"])
  else:
    return "{} already in database!".format(msg_author.id)
  """

def set_color(message):
  msg_author = message.author
  str_auth_id = str(msg_author.id)
  values = message.content.lstrip(">").split()
  if str_auth_id in db.keys():
    rgb_color = hex_to_rgb(values[1])
    color = discord.Colour.from_rgb(rgb_color[0], rgb_color[1], rgb_color[2])
    my_dict = db[str_auth_id]
    my_dict["color"] = color
    db[str_auth_id] = my_dict
    #db[str_auth_id]["color"] = color
    return "color successfully changed to {}!".format(values[1])
  else:
    return "{} doesn't exist in database, run >start command to get started".format(msg_author)

def display(message):
  msg_author = message.author
  str_auth_id = str(msg_author.id)
  if str_auth_id in db.keys():
    embed = discord.Embed(
      title="{}'s profile".format(msg_author.display_name),
      colour=db[str_auth_id]["color"],
      description="balance: {}".format(db[str_auth_id]["bal"])
    )
    embed.add_field(name="kudos:", value=db[str_auth_id]["kudos"], inline=True)
    embed.add_field(name="capybara count:", value=db[str_auth_id]["capybara_count"], inline=True)
    embed.set_author(name=msg_author, icon_url=msg_author.avatar_url)
    return embed

def remove(message):
  msg_author = message.author
  str_auth_id = str(msg_author.id)
  if str_auth_id in db.keys():
    del db[str_auth_id]
    return "{} successfully removed".format(msg_author)
  else:
    return "{} doesn't exist in database, run >start command to get started".format(msg_author)

methods = {
  "start": start,
  "set_color": set_color,
  "display": display,
  "remove": remove
  }