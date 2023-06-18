import discord
from discord.ext import commands
import os
import sys
import json

FilePath = os.path.dirname(os.path.abspath(__file__))
intents = discord.Intents.all()
bot = discord.Client(intents=intents)

def LoadGates():
    if sys.platform.startswith("lin"):
        with open(f"{FilePath}/Files/Gates.json", "r") as JSON:
            return json.load(JSON)
    if sys.platform.startswith("win"):
        with open(rf"{FilePath}\Files\Gates.json", "r") as JSON:
            return json.load(JSON)

class GateKeeperBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(aliases=["MakeGate", "Gate"])
    async def SetGate(self, ctx, GateName):
        await ctx.message.delete()
        RawGates=LoadGates()
        VRole = discord.utils.get(ctx.guild.roles, name=RawGates[GateName]["Role"])
        if VRole == None:
            VRole = await ctx.guild.create_role(name=RawGates[GateName]["Role"], hoist=False, mentionable=False)

        async def EntranceButtonCallback(interaction):
            VRole = discord.utils.get(ctx.guild.roles, name=RawGates[GateName]["Role"])
            await interaction.response.defer()
            if not interaction.user.get_role(VRole.id):
                await interaction.user.add_roles(VRole)
            else:
                await interaction.user.remove_roles(VRole)

        GateView = discord.ui.View()
        EntranceButton = discord.ui.Button(label="Entrance")
        EntranceButton.callback = EntranceButtonCallback
        GateView.add_item(EntranceButton)
        GateEmbed= discord.Embed(title=RawGates[GateName]["Title"],
                                 description=RawGates[GateName]["Text"])
        GateMessage = await ctx.channel.send(embed=GateEmbed, view=GateView)
async def setup(bot):
    await bot.add_cog(GateKeeperBot(bot))


