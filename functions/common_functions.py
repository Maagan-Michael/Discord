from app import bot
import random
import requests
import time
import discord
from discord.ui import Button,View




@bot.command(name="arrow")
async def arrow(ctx, size):
    response = ""
    for i in range(int(size)):
        response = response + ("#" * i + "\n")

    for i in  range(int(size), 0, -1):
        response = response + ("#" * i + "\n")


    await ctx.send(response)



@bot.command(name="nevo_coins")
async def nevo_coins(ctx):
    response = "You got "  + str(random.randint(1,1000))+ " nevo coins"

    await ctx.send(response)


@bot.command(name="rand_name")
async def random_name(ctx):
    ls = ["Itay", "Nevo", "Yonatan K.", "Yuval" ,"Bonti", "kami"]
    response = random.choice(ls)
    await ctx.send(response)


@bot.command(name="dog")
async def button(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    b1 = Button(label="תן לי כלב", style=discord.ButtonStyle.blurple)
    async def button_callback(interaction):
        await interaction.response.edit_message(content="got your dog", view = None)
        await ctx.send(image_link)
    b1.callback = button_callback
    view = View()
    view.add_item(b1)

    await ctx.send("want a dog?", view=view)


@bot.command(name="zebra")
async def random_dog_pic(ctx):
    await ctx.send("https://media.tenor.com/_BQfXFMQVtkAAAAC/zebra-zebras.gif")

@bot.command(name="dice")
async def roll_dice(ctx):
    rand_num1 = random.randint(1,6)
    rand_num2 = random.randint(1,6)
    await ctx.send(str(rand_num1)+str(rand_num2))

@bot.command(name="kids")
async def random_dog_pic(ctx, name):
    if name == "קלק":
        await ctx.send("https://ibasketball.co.il/wp-content/uploads/2020/10/S106561-103x128.jpg")
    
    elif name=="נבו":
        await ctx.send("https://ibasketball.co.il/wp-content/uploads/2020/10/S106575-747x1024.jpg")

    elif name=="עמית":
        await ctx.send("https://firebasestorage.googleapis.com/v0/b/mm-discord.appspot.com/o/unknown.png?alt=media&token=ffb3e02d-342f-41cd-9b12-97cf3cdb258a")

    elif name=="איתי":
        await ctx.send("https://firebasestorage.googleapis.com/v0/b/mm-discord.appspot.com/o/20220626_004533.jpg?alt=media&token=b7799622-289b-42db-93a3-2f0836e8a5b0")
@bot.command(name="bomb")
async def bomb(ctx, num):
        x = int(num)

        while True:
            await ctx.send(x)
            x-= 1
            time.sleep(1)
            if x == 0:
            
                break
            elif x < 0:
                break
        await ctx.send(f"https://media.tenor.com/-g-Um3DDvV0AAAAC/explosion.gif")
    

@bot.command(name="gal")
async def barkan(ctx, name):
    if name == "barkan":
        await ctx.send("https://cdn.discordapp.com/attachments/1024725516667867196/1054403616263376906/IMG_0640.png")


@bot.command(name="superS")
async def barkan(ctx):
        await ctx.send(r"https://firebasestorage.googleapis.com/v0/b/mm-discord.appspot.com/o/WhatsApp%20Video%202022-11-05%20at%2016.52.18.mp4?alt=media&token=b150891c-e3f6-486d-909d-c96ce968fbda")


