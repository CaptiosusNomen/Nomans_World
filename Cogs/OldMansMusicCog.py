import discord
from discord.ext import commands
import os
FilePath = os.path.dirname(os.path.abspath(__file__))
from asyncio import sleep

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

class OldMansMusic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.MusicChannel = None
        self.IsPlaying=False

    @commands.is_owner()
    @commands.command(pass_context=True)
    async def PlaySong(self, ctx):
        await ctx.message.delete()
        if self.IsPlaying==False:
            everyone = ctx.guild.default_role
            self.MusicChannel = await ctx.guild.create_voice_channel(f"Old_Mans_Music ", overwrites={
                everyone: discord.PermissionOverwrite(read_messages=True, send_messages=False)},
                                                             user_limit=16,
                                                             position=ctx.channel.position+1)
            self.Voice = await self.MusicChannel.connect(self_deaf=True)
            self.Voice.play(discord.FFmpegPCMAudio(source=f"{FilePath}\\Files\\Tears.mp3"))
            self.IsPlaying = True
            await sleep(80)
            self.IsPlaying = False
            await self.MusicChannel.delete()


async def setup(bot):
    await bot.add_cog(OldMansMusic(bot))


