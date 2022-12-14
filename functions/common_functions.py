from app import bot
import random
import requests
import time




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
async def random_dog_pic(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await ctx.send(image_link)


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
        ctx.send("boom!!!!!!!!!!")
    
