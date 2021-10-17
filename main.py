import os
import discord 
import json
import requests
from keep_alive import keep_alive




my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$office'):
    response = requests.get("https://officeapi.dev/api/quotes/random")
    quote = json.loads(response.text)
    filter_quote = quote.get('data').get('content')+" -"+quote.get('data').get('character').get('firstname')+" "+quote.get('data').get('character').get('lastname')
    await message.channel.send(filter_quote)
    
keep_alive()
client.run(my_secret)