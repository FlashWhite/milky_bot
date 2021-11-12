import discord
import random
from milky_bot.resources import bs

def capybara_embed(message, random_channel):
  msg_author = message.author
  embed = discord.Embed(
    title="congratulations *{}* !!! u started a capybara party in da #{} :]".format(msg_author.display_name, random_channel),
    author=msg_author.display_name,
    colour=000000,
    description="yeah yeah wooo capybaras!!!"
    )
  embed.set_author(name=msg_author, icon_url=msg_author.avatar_url)
  embed.set_image(url=random.choice(bs.capybara_gifs))
  embed.add_field(name="CAPY", value="♬♩♪♩", inline=True)
  embed.add_field(name="BARA", value="♩♪♩♬", inline=True)
  embed.add_field(name="PARTY!!!!", value="♬♩♪♩", inline=True)
  embed.add_field(name="✧･ﾟ: ✧･ﾟ: 　　 :･ﾟ✧:･ﾟ✧", value="mm yes coconut doggys", inline=False)
  #embed.timestamp = datetime.utcnow().isoformat()
  embed.set_footer(text="thank you for running da capybara command")
  return embed

  #SyntaxError: 'await' outside async function
  #await must occur within async func?
  #await random_channel.send("", tts=True, embed=embed)