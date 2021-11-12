import discord

def capybara_embed(message):
  random_channel = message.channel
  embed = discord.Embed(
    title="capybara",
    author=message.author.nick,
    colour=000000,
    description="capybara party in da {}!!!!".format(random_channel)
    )
  embed.set_image(message.author.avatar_url)
  #SyntaxError: 'await' outside async function
  #await must occur within async func?
  #await random_channel.send("", tts=True, embed=embed)