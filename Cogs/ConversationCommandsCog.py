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

    @commands.is_owner()
    @commands.command(pass_context=True)
    async def PlaySong(self, ctx):
        channel = discord.utils.get(ctx.guild.voice_channels, name='Old_Mans_Music')
        if channel is None:
            everyone = ctx.guild.default_role
            MusicChannel = await ctx.guild.create_voice_channel(f"Old_Mans_Music", overwrites={
                everyone: discord.PermissionOverwrite(read_messages=True, send_messages=False)},
                                                             user_limit=16,category=ctx.channel.category,
                                                             position=ctx.channel.position+1)
            Voice = await MusicChannel.connect(self_deaf=True)
            await sleep(3)
            Voice.play(discord.FFmpegPCMAudio(source=f"{FilePath}\\Files\\Tears.mp3"))
            await sleep(80)
            await Voice.disconnect()
            await MusicChannel.delete()


async def setup(bot):
    await bot.add_cog(ConversationCommands(bot))


