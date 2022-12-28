from app import bot
import random
import requests
import time
import discord
from discord.ui import Button,View





@bot.command(name="game")
async def game(ctx):

    user_mention = ctx.author.mention
    user_id = ctx.author.id

    url = f"https://mm-discord-default-rtdb.europe-west1.firebasedatabase.app/users/{user_id}.json"
    response = requests.get(url)
    user_data = response.json()
    if user_data == None:
        #creates user
        user_data = {"stars":0, "shmekels": 0, "gems": 0}
        requests.patch(url,json=user_data)



   
        


    buy_button = Button(label="Buy Gem",style=discord.ButtonStyle.primary)
    sell_button = Button(label="Sell Gem",style=discord.ButtonStyle.danger)

    

    async def buy_star(interaction):
        await interaction.response.send_message(content="buy gem" )

   

    async def sell_star(interaction):
        await interaction.response.send_message(content="sell gem")
   

   
    buy_button.callback = buy_star
    sell_button.callback = sell_star

    view = View()
    view.add_item(buy_star)
    view.add_item(sell_star)

    await ctx.send(f"Here is your account details {user_mention} :\n Smekels: {user_data['shmekels']}\n Gems: {user_data['gems']} \n Stars: {user_data['stars']} \n\n You can buy a Gem for 50 Shmekels\nYou can sell a Gem for 25 Shmekels", view=view)
