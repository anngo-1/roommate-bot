# importing 
from botfunc import *
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



@client.event
async def on_ready():
    #status for commands
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='!functions'))
    #checks
    print("bot ready")



@client.event
async def on_message(message):
    check = message.author.id != client.user.id

    for i in commandlist:
        if message.content[1:message.content.find(" ")] in i.functions:
            if message.content.find(" ") == -1:
                try:
                    func = getattr(i, message.content[1:])
                except: 
                    message.channel.send("Incorrect functions syntax. Please see !functions")
            else:
                try: 
                    func = getattr(i, message.content[1:message.content.find(" ")])
                except:
                    message.channel.send("Incorrect functions syntax. Please see !functions")
            argslist = message.content.split(" ")
            x = None
            y= None
            z= None
      
            try: 
                w = str(message.author.id)
                x = argslist[1]
                y = argslist[2]
                z = " ".join(argslist[3:])
            except:
                    
                print(None)
                    
                                    
          
           
            await message.channel.send(func(w, x, y, z))
    
    if message.content.startswith("!functions") and check:
        commands = ""
        for i in commandlist:
            commands += ("```\n" + i.name + "\n\n" + i.desc + "\n" + "\n" + "\n" + i.functions + '```' )
            

        await message.channel.send(commands)
        


    if message.content == "hello" and check:
        await messagefunc(client, message.channel, "hi")














#  runs bot using token from env file 
client.run(DISCORD_TOKEN)
