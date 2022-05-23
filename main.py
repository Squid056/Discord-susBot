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
  #emoji = '\N{THUMBS UP SIGN}'
  emoji = '👨‍🦯'
  if message.author == client.user:
    await message.add_reaction(emoji)
    return

  if message.content.startswith('sus'):
    await message.channel.send('ඞ')

  if message.content.startswith('hi'):
    await message.author.send('👀')


token = os.environ['BotToken']
client.run(token)
