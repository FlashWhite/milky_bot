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
from milky_bot import economy

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
  
  if msg.startswith("clear"):
    for key in db.keys():
      del db[key]
    await message.channel.send("cleared")

  if msg.startswith("db"):
    for key in db.keys():
      await message.channel.send(db[key])

  if msg.startswith("<"):
    values = msg.lstrip("<").split()
    if values[0] in profile.methods:
      output = profile.methods[values[0]](message)
      if type(output) == str:
        await message.channel.send(output)
      elif type(output) == discord.Embed:
        await message.channel.send("", embed=output)
  if msg.startswith(">"):
    if str(msg_author) in db.keys():
      values = msg.lstrip(">").split()
      if values[0] in profile.methods:
        output = profile.methods[values[0]](message)
        if type(output) == str:
          await message.channel.send(output)
        elif type(output) == discord.Embed:
          await message.channel.send("", embed=output)
    else:
      await message.channel.send("", embed=profile.welcome(message))
    """
    command = values[0]
    if command == "start":
      await message.channel.send(profile.start(message))
    elif command == "set_color":
      await message.channel.send(profile.set_color(message))
    elif command == "display":
      #catch exception where profile isn't created
      await message.channel.send("", embed=profile.display(message))
    elif command == "remove":
      await message.channel.send(profile.remove(message))
    elif command == "capybara":
      #check bot permissions to randomize sends only in text_channels it has permission to
      random_channel = random.choice(message.guild.text_channels)
      await random_channel.send("capybara party time!", tts=True, embed=capybara.capybara_embed(message, random_channel))
    elif command == "echo":
      profile.echo(message, values[1])
    else:
      await message.channel.send("no command for {} found".format(values[0]))
    """

  if msg.startswith("-setbalance"):
    values = msg.lstrip("-setbalance ").split()
    if values == []:
      await message.channel.send("To use setbalance, you need to add the balance after the command! Ex: -setbalance 10")
    else:
      await message.channel.send(economy.set_balance(message, values[0]))
  
  if msg.startswith("-balance"):
    await message.channel.send(economy.get_balance(message))
  
  if msg.startswith("-gamble"):
    await message.channel.send(economy.gamble(message))
  
  if msg.startswith("-welcome"):
    await message.channel.send(profile.welcome(message))
  
  if msg.startswith("-inituser"):
    await message.channel.send(profile.init_user(message))

  if msg.startswith("-profile"):
    await message.channel.send(profile.display_profile(message))

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