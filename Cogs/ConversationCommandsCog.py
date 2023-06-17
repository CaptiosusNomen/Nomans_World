import discord
from discord.ext import commands
import os
FilePath = os.path.dirname(os.path.abspath(__file__))
from asyncio import sleep

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

class ConversationCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.MusicChannel = None
        self.OldManIsPlaying = False

    @commands.is_owner()
    @commands.command(pass_context=True)
    async def PlaySong(self, ctx):
        if self.OldManIsPlaying==False:
            everyone = ctx.guild.default_role
            self.MusicChannel = await ctx.guild.create_voice_channel(f"Old_Mans_Music ", overwrites={
                everyone: discord.PermissionOverwrite(read_messages=True, send_messages=False)},
                                                             user_limit=16,category=ctx.channel.category,
                                                             position=ctx.channel.position+1)
            self.Voice = await self.MusicChannel.connect(self_deaf=True)
            self.Voice.play(discord.FFmpegPCMAudio(source=f"{FilePath}\\Files\\Tears.mp3"))
            self.OldManIsPlaying = True
            await sleep(80)
            self.OldManIsPlaying = False
            await self.Voice.disconnect()
            await self.MusicChannel.delete()


async def setup(bot):
    await bot.add_cog(ConversationCommands(bot))


