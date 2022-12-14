from app import bot
import random
import requests
import time
import discord
from discord.ui import Button,View

async def check_user_data(user_id):
    url = f"https://mm-discord-default-rtdb.europe-west1.firebasedatabase.app/users/{user_id}.json"
    response = requests.get(url)
    user_data = response.json()
    if user_data == None:
        #creates user
        user_data = {"stars":0, "shmekels": 0, "gems": 0}
        requests.patch(url,json=user_data)

    return user_data

async def get_shmekels(user_id, amount):
    url = f"https://mm-discord-default-rtdb.europe-west1.firebasedatabase.app/users/{user_id}.json"
    user_data = await check_user_data(user_id)

    user_data["shmekels"] = user_data["shmekels"] + amount
    requests.patch(url,json=user_data)


def check_result(choice1, choice2):
        if choice1 == "rock" and choice2 == "rock" or choice1 == "paper" and choice2 == "paper" or choice1 == "scissors" and choice2 == "scissors":
            return (0, choice1, choice2)

        elif choice1 == "rock" and choice2 == "scissors" or choice1 == "paper" and choice2 == "rock" or choice1 == "scissors" and choice2 == "paper":
            return (1, choice1, choice2)

        elif choice1 == "paper" and choice2 == "scissors" or choice1 == "scissors" and choice2 == "rock" or choice1 == "rock" and choice2 == "paper":
            return (2, choice1, choice2)





@bot.command(name="rps")
async def rock_paper_scissors(ctx):

    user_mention = ctx.author.mention
    user_id = ctx.author.id
    print(user_id)
    bot_choice = random.choice(["rock", "paper", "scissors"])

    async def process_result(result):
        
        await ctx.send("bot choice " + result[2])
        if result[0] == 0:
            await ctx.send("its a tie! both players picked " + result[1])
        
        elif result[0] == 1:
            await get_shmekels(user_id=user_id,amount=5)
            await ctx.send(f"{user_mention} you won!!\n\n heres 5 Shmekels, enjoy!")

        elif result[0] == 2:
            await ctx.send("better luck next time...")

        


    rock_button = Button(label="Rock",style=discord.ButtonStyle.primary)
    paper_button = Button(label="Paper",style=discord.ButtonStyle.danger)
    scissors_button = Button(label="Scissors",style=discord.ButtonStyle.success)

    async def on_rock(interaction):
        await interaction.response.edit_message(content="choice: rock" , view = None)
        result = check_result("rock", bot_choice)
        await process_result(result)

    async def on_paper(interaction):
        await interaction.response.edit_message(content="choice: paper" , view = None)
        result = check_result("paper", bot_choice)
        await process_result(result)

    async def on_scissors(interaction):
        await interaction.response.edit_message(content="choice:  scissors" , view = None)
        result = check_result("scissors", bot_choice)
        await process_result(result)

    rock_button.callback = on_rock
    paper_button.callback = on_paper
    scissors_button.callback = on_scissors

    view = View()
    view.add_item(rock_button)
    view.add_item(paper_button)
    view.add_item(scissors_button)

    await ctx.send("lets see if you can win", view=view)
