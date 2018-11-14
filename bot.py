import discord
from discord.ext import commands

#Insert your own discord bot token.

TOKEN = ""

client = commands.Bot(command_prefix = "&")
client.remove_command('help')

@client.event
async def on_ready():
    print ("Bot is ready to go!")


#----------------------------------------------------------    

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}: {}'.format(author, content))

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}: {}'.format(author, content))

client.run(TOKEN)
