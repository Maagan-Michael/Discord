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


async def buy_gem(user_id):
    url = f"https://mm-discord-default-rtdb.europe-west1.firebasedatabase.app/users/{user_id}.json"
    response = requests.get(url)
    user_data = response.json()
    shmekels = user_data["shmekels"]
    if shmekels >= 25:
        user_data["shmekels"] = user_data["shmekels"] - 25
        user_data["gems"] = user_data["gems"] + 1
        requests.patch(url,json=user_data)
        return True
    else:
        return False

async def sell_gem(user_id):
    url = f"https://mm-discord-default-rtdb.europe-west1.firebasedatabase.app/users/{user_id}.json"

    user_data = await  check_user_data(user_id)
    gems = user_data["gems"]
    if gems > 0:
        user_data["gems"] = user_data["gems"] - 1
        user_data["shmekels"] = user_data["shmekels"] + 10

        requests.patch(url,json=user_data)
        return True
    else:
        return False




   


@bot.command(name="game")
async def game(ctx):

    user_mention = ctx.author.mention
    user_id = ctx.author.id
    user_data = await check_user_data(user_id)

   



   

    buy_button = Button(label="Buy Gem",style=discord.ButtonStyle.primary)
    sell_button = Button(label="Sell Gem",style=discord.ButtonStyle.danger)

    

    async def buy_star(interaction):
        result = await buy_gem(user_id)

        if result == True:
            await interaction.response.send_message(content=f"{user_mention} bought a Gem!" )
        else: 
            await interaction.response.send_message(content=f"{user_mention} you dont have enough Shmekels to buy a Gem!" )
            


    async def sell_star(interaction):
        result = await sell_gem(user_id)
        if result == True:
            await interaction.response.send_message(content=f"{user_mention} sold a Gem!" )
        else: 
            await interaction.response.send_message(content=f"{user_mention} you dont have any Gems!" )
   

   
    buy_button.callback = buy_star
    sell_button.callback = sell_star

    view = View()
    view.add_item(buy_button)
    view.add_item(sell_button)

    await ctx.send(f"Here is your account details {user_mention} :\n Smekels: {user_data['shmekels']}\n Gems: {user_data['gems']} \n Stars: {user_data['stars']} \n\n You can buy a Gem for 50 Shmekels\nYou can sell a Gem for 25 Shmekels", view=view)
