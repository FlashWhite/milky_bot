import discord
import os
import random

#import asyncio
#import time
#import string
from replit import db
from milky_bot.inspire_bot import inspire
#from milky_bot.resources import bs
from milky_bot import profile
#from datetime import datetime
from milky_bot import capybara

client = discord.Client()

evan_is_the_best = ["ur so cool evan", "audrey sux"]

if "responding" not in db.keys():
  db["responding"] = True

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  msg_author = message.author

  if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check, timeout=10 )
        await channel.send('Hello {.author}!'.format(msg))
  
  #does not save user data after bot stops running
  if msg.startswith(">"):
    values = msg.lstrip(">").split()
    #implement directly calling method with name given in values[0]
    command = values[0]
    if command == "start":
      await message.channel.send(profile.start(msg_author, values))
    elif command == "display":
      #catch exception where profile isn't created
      await message.channel.send("", embed=profile.display(msg_author))
    elif command == "capybara":
      #check bot permissions to randomize sends only in text_channels it has permission to
      random_channel = random.choice(message.guild.text_channels)
      await random_channel.send("capybara party time!", tts=True, embed=capybara.capybara_embed(message, random_channel))
    else:
      await message.channel.send("no command for {} found".format(values[0]))

  if msg.startswith(">id"):
    await message.channel.send("message author: {}, author nick: {}".format(msg_author, msg_author.display_name))
  
  if msg.startswith("$inspire"):
    quote = inspire.get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = inspire.starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in inspire.sad_words):
      #i do a little trolling
      if message.author.id == 291351371612160010:
        await message.channel.send(random.choice(evan_is_the_best))
      else:
        await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    inspire.update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      inspire.delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

client.run(os.environ["TOKEN"])
#client.run(os.getenv("TOKEN"))