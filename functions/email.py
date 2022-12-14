from app import bot


@bot.command(name="email")
async def arrow(ctx, to_email, subject, message):
    await ctx.send("this functions is removed for now" )
    