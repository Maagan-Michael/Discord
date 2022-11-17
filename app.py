from os import getenv
import discord
from discord.ext import commands

import random
import music

TOKEN = getenv("TOKEN")
TOKEN = "MTA0MjM2ODc3Njk2NTk4ODM3Mg.GYxGGm.WkB2fupv32OyX-SzB7N082mLEkpU1QUHGpi4cs"

intents = discord.Intents.all()
intents.dm_messages = True
intents.emojis_and_stickers = True
intents.message_content = True
intents.members = True
intents.messages = True


# cogs = [music]

bot = commands.Bot(command_prefix="!", intents=intents)


# for i in range(len(cogs)):
    # cogs[i].setup(bot)


@bot.event
async def on_ready():
    print("we have logged in as {0.user}".format(bot))



@bot.command(name="arrow")
async def arrow(ctx, size):
    response = ""
    for i in range(int(size)):
        response = response + ("?" * i + "\n")

    for i in  range(int(size), 0, -1):
        response = response + ("?" * i + "\n")

    await ctx.send(response)



@bot.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    chanel = str(message.channel.name)
    print(user_message)
    print(username)
    print(chanel)

    if message.author == bot.user:
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


    await bot.process_commands(message)





bot.run(token=TOKEN)
