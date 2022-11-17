from os import getenv
import discord

import random

TOKEN = getenv("TOKEN")

intents = discord.Intents.all()
intents.dm_messages = True
intents.emojis_and_stickers = True
intents.message_content = True
intents.members = True
intents.messages = True


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))




@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    chanel = str(message.channel.name)
    print(user_message)
    print(username)
    print(chanel)

    if message.author == client.user:
        return

    if message.channel.name == "general":
        if user_message.lower() == "hello":
            await message.channel.send(f"hello {username}")
            return

        elif user_message.lower() == "bye":
            await message.channel.send(f"bye bye {username}")
            return

        
        elif user_message.lower() == "!random":
            response = f"Your random number is: " + str(random.randint(1,10000))
            await message.channel.send(response)
            return






client.run(token=TOKEN)
