# importing 
from inspect import getmembers, isfunction

import botfunc
import discord
import os
from dotenv import load_dotenv
# load secrent .env using dotenv
load_dotenv()
# token bruh
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# create bot
intents = discord.Intents.default()
client = discord.Client(intents = intents)
intents.message_content = True


#command list comprehension
functuple = getmembers(botfunc, isfunction)
commandlist = [i[0] for i in functuple]
print (commandlist)



@client.event
async def on_ready():
    #status for commands
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='!commands'))
    #checks
    print("bot ready")



@client.event
async def on_message(message):
    check = message.author.id != client.user.id

    if message.content.startswith("!commands") and check:
        commands = ""
        for i in commandlist:
            commands += (i + "," + " ")

        await message.channel.send(commands)
        


    if message.content == "hello" and check:
        await message.channel.send('wassup')














#  runs bot using token from env file 
client.run(DISCORD_TOKEN)
