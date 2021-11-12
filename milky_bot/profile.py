import discord
from milky_bot.resources import bs
#switch to database later
#from replit import db

#throw error if color not provided
def start(msg_author, values):
  bs.users[msg_author.id] = {"bal":0, "color":int(values[1])}
  return "added {} with balance {} and color {}".format(msg_author, bs.users[msg_author.id]["bal"], bs.users[msg_author.id]["color"])

def display(msg_author):
  if msg_author.id in bs.users:
    embed = discord.Embed(
      title="{}'s profile".format(msg_author),
      colour=bs.users[msg_author.id]["color"],
      description="balance: {}".format(bs.users[msg_author.id]["bal"])
    )
    embed.set_author(name=msg_author, icon_url=msg_author.avatar_url)
    return embed
