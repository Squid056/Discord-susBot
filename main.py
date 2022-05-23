import os
import discord 

#client log and watching status 
activity = discord.Activity(name='you', type=discord.ActivityType.watching)
client = discord.Client(activity=activity)

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))



# on message sus say 
@client.event
async def on_message(message):
  emoji = '\N{THUMBS UP SIGN}'
  if message.author == client.user:
    return

  if message.content.startswith('sus'):
    await message.channel.send('ඞ')
    await message.add_reaction(emoji)



token = os.environ['BotToken']
client.run(token)
