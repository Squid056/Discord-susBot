import os
import discord 

#client = discord.Client()
activity = discord.Activity(name='you', type=discord.ActivityType.watching)
client = discord.Client(activity=activity)

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('sus'):
    await message.channel.send('ඞ')



token = os.environ['BotToken']
client.run(token)
