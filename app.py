from os import getenv
import discord
from discord.ext import commands

import random
import send_email
import music

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



@bot.command(name="arrow")
async def arrow(ctx, size):
    response = ""
    for i in range(int(size)):
        response = response + ("#" * i + "\n")

    for i in  range(int(size), 0, -1):
        response = response + ("#" * i + "\n")


    await ctx.send(response)


@bot.command(name="nevo")
async def arrow(ctx):
    response = "You got "  + str(random.randint(1,1000))+ " nevo coins"

    await ctx.send(response)


@bot.command(name="rand_name")
async def arrow(ctx):
    ls = ["Itay", "Nevo", "Yonatan K.", "Yuval" ,"Bonti", "kami"]
    response = random.choice(ls)
    await ctx.send(response)


@bot.command(name="email")
async def arrow(ctx, to_email, subject, message):

    send_email.send_mail(to_email,subject,message)
    await ctx.send("email has been sent to " + to_email)
    



@bot.event
async def on_message(message):
    username = message.author.mention
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
