import os
import discord 
from upkeep  import keep_alive


token = os.environ['BotToken']
activity = discord.Activity(name='you', type=discord.ActivityType.watching)
client = discord.Client(activity=activity)
embed = discord.Embed()
embed.set_image(url="https://media.discordapp.net/attachments/890017011780964442/976759712508964864/smoke-smoking.gif")

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

# on message sus say 
@client.event
async def on_message(message):
  emoji = '👨‍🦯'
  if message.author == client.user:
    return

  if message.content.startswith('sus'):
    await message.channel.send('ඞ')
    await message.add_reaction(emoji)

  if message.content.startswith('hi'):
    await message.author.send('👀')
  
  if message.content.startswith('jalopenos'):
    await message.channel.send(embed=embed)
  

keep_alive()
client.run(token)
