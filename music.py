import discord
from discord.ext import commands
import youtube_dl



class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.command(name="join")
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("you're not in a voice channel!")
        
        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()
        
        else:
            await ctx.voice_client.move_to(voice_channel)


    @commands.command(name="disconnect")
    async def disconnect(self,ctx):
            await ctx.voice_client.disconnect()



    @commands.command(name="play")
    async def play(self,ctx):
        ctx.voice_client.stop()
        FFMEPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconect_delay_max 5', 'options':'-vn'}
        YDL_OPTIONS = {"format": ' bestaudio'}

        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url,download=False)
            url2 = info["formats"][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMEPEG_OPTIONS)
            vc.play(source)

   
   
    @commands.command(name="pause")
    async def pause(self,ctx):
            await ctx.voice_client.pause()
            await ctx.send("paused!!!")


    @commands.command(name= "resume")
    async def resumed(self,ctx):
            await ctx.voice_client.resumed()
            await ctx.send("resumed!!!")



async def setup(client):
    await client.add_cog(music(client))