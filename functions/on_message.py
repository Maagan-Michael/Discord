from app import bot


@bot.event
async def on_message(message):
    username = message.author.mention
    user_message = str(message.content)
    chanel = str(message.channel.name)


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