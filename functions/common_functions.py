from app import bot
import random



@bot.command(name="arrow")
async def arrow(ctx, size):
    response = ""
    for i in range(int(size)):
        response = response + ("#" * i + "\n")

    for i in  range(int(size), 0, -1):
        response = response + ("#" * i + "\n")


    await ctx.send(response)



@bot.command(name="nevo coins")
async def arrow(ctx):
    response = "You got "  + str(random.randint(1,1000))+ " nevo coins"

    await ctx.send(response)


@bot.command(name="rand_name")
async def arrow(ctx):
    ls = ["Itay", "Nevo", "Yonatan K.", "Yuval" ,"Bonti", "kami"]
    response = random.choice(ls)
    await ctx.send(response)
