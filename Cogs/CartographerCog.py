import discord
from discord.ext import commands
import os
import json
import time
import random
import sys
from Cogs.StoryBoardDisplayCog import StoryBoardDisplay , ColorPicker
from Cogs.Storyboard import SBImageAssembly




FilePath = os.path.dirname(os.path.abspath(__file__))
intents = discord.Intents.all()
bot = discord.Client(intents=intents)


def LoadMap():
    if sys.platform == "linux" or sys.platform == "linux2":
        with open(f"{FilePath}/Files/Map.json", "r") as JSON:
            return json.load(JSON)
    if sys.platform == "win32" or sys.platform == "win64":
        with open(f"{FilePath}\\Files\\Map.json", "r") as JSON:
            return json.load(JSON)


class NaniteBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.is_owner()
    @commands.command(aliases=["Make", "Make The", "Make My", "Create The", "Create My", "Let There Be"],
                      pass_context=True)
    async def Create(self, ctx, PlaceToMake):
        await ctx.message.delete()
        self.Map=LoadMap()
        everyone = ctx.guild.default_role
        NewLocation = await ctx.guild.create_category(PlaceToMake)
        for Location in self.Map[PlaceToMake]:
            NewChannel = await ctx.guild.create_text_channel(f"{Location}", overwrites={
                everyone: discord.PermissionOverwrite(read_messages=True, send_messages=False)},
                                                             topic=self.Map[PlaceToMake][Location]["Topic"],
                                                             category=NewLocation)
            LocationEmbed = discord.Embed(colour=0x31f25c,
                                  description=self.Map[PlaceToMake][Location]["Description"])
            try:
                if sys.platform == "linux" or sys.platform == "linux2":
                    Image=discord.File(f"{FilePath}/Files/Images/Locations/{self.Map[PlaceToMake][Location]['Image']}.jpg")
                    LocationEmbed.set_image(url=f"attachment://{FilePath}/Files/Images/Locations/{self.Map[PlaceToMake][Location]['Image']}.jpg")
                if sys.platform == "win32" or sys.platform == "win64":
                    Image=discord.File(f"{FilePath}\\Files\\Images\\Locations\\{self.Map[PlaceToMake][Location]['Image']}.jpg")
                    LocationEmbed.set_image(url=f"attachment://{FilePath}\\Files\\Images\\Locations\\{self.Map[PlaceToMake][Location]['Image']}.jpg")
            except FileNotFoundError:
                if sys.platform == "linux" or sys.platform == "linux2":
                    Image=discord.File(f"{FilePath}/Files/Images/Locations/{self.Map[PlaceToMake][Location]['Image']}.png")
                    LocationEmbed.set_image(url=f"attachment://{FilePath}/Files/Images/Locations/{self.Map[PlaceToMake][Location]['Image']}.png")
                if sys.platform == "win32" or sys.platform == "win64":
                    Image=discord.File(f"{FilePath}\\Files\\Images\\Locations\\{self.Map[PlaceToMake][Location]['Image']}.png")
                    LocationEmbed.set_image(url=f"attachment://{FilePath}\\Files\\Images\\Locations\\{self.Map[PlaceToMake][Location]['Image']}.png")


            LocationView = discord.ui.View()
            for NPC in self.Map[PlaceToMake][Location]["NPC"]:
                print(NPC)
                NPCButton=discord.ui.Button(label=NPC)
                async def NPCButtonCallback(interaction):
                    Choices = SBImageAssembly(NPC,"Start")
                    TempFile = discord.File(f"{FilePath}\\Files\\Images\\TEMP.png", filename="TEMP.png")
                    SBView = discord.ui.View()
                    Inventory = {}
                    for each in Choices:
                        if each == "Scenario":
                            pass
                        else:
                            Style = ColorPicker(Choices, each)
                            ChoiceButton = discord.ui.Button(label=each,
                                                             custom_id=f"{Choices['Scenario']},{Choices[each]['Destination']},{Inventory}",
                                                             style=Style)
                            ChoiceButton.callback = StoryBoardDisplay.ChoiceButtonCallback
                            SBView.add_item(ChoiceButton)
                    await interaction.response.send_message(ephemeral=True, file=TempFile, view=SBView)

                LocationView.add_item(NPCButton)
                NPCButton.callback = NPCButtonCallback

            await NewChannel.send(embed=LocationEmbed,view=LocationView,file=Image)


async def setup(bot):
    await bot.add_cog(NaniteBot(bot))


