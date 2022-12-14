from os import getenv
import discord
from discord.ext import commands
from functions.common_functions import *

import random


TOKEN = getenv("TOKEN")

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



exec(open("./functions/common_functions.py").read())
exec(open("./functions/on_message.py").read())








bot.run(token=TOKEN)
