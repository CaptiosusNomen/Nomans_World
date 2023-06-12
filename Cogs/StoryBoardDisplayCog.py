import discord
from discord.ext import commands
from Cogs.Storyboard import SBImageAssembly,GetSBInfo
import os
import ast

FilePath = os.path.dirname(os.path.abspath(__file__))
intents = discord.Intents.all()
bot = discord.Client(intents=intents)

class StoryBoardDisplay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def ColorPicker(self,Choices,each):
        if Choices[each]['Color'] == "green":
            Style = discord.ButtonStyle.green
        elif Choices[each]['Color'] == "grey":
            Style = discord.ButtonStyle.grey
        elif Choices[each]['Color'] == "red":
            Style = discord.ButtonStyle.red
        elif Choices[each]['Color'] == "blurple":
            Style = discord.ButtonStyle.blurple
        return Style

    @commands.is_owner()
    @commands.command(pass_context=True)
    async def Demo(self, ctx):
        await ctx.message.delete()
        await self.StoryBoardDisplayMessage(ctx.channel,"2-C", "10")

    @commands.is_owner()
    @commands.command(pass_context=True)
    async def SBTest(self, ctx):
        await ctx.message.delete()
        await self.StoryBoardDisplayMessage(ctx.channel,"TestStory", "10")


    async def StoryBoardDisplayMessage(self, channel, Scenario, Act):
        RawData = GetSBInfo(Scenario=Scenario,GetFullStory=True)
        Embed = discord.Embed(title=RawData[Scenario]["Info"]["Name"],
        description=RawData[Scenario]["Info"]["Description"])

        View = discord.ui.View()
        SBLaunchButton = discord.ui.Button(label="Start", custom_id=f"{Scenario},{Act}")

        async def EndButtonCallback(interaction):
            Data = interaction.data['custom_id'].split(",")
            await interaction.response.edit_message(view=None)
            await interaction.channel.send(f"{interaction.user.name} has finished {Data[0]} with a ranking of {Data[1]} and found {Data[2]}")

        async def ChoiceButtonCallback(interaction):
            Data = interaction.data['custom_id'].split(",")
            Inventory = ast.literal_eval(Data[2])
            try:
                if Data[3]!=None:
                    InvintoryUpdate = Data[3].split(":")
                    Items = InvintoryUpdate[1].split(",")
                    if InvintoryUpdate[0]=="Price":
                        for each in Items:
                            Inventory.pop(each,None)
                    if InvintoryUpdate[0]=="Reward":
                        for each in Items:
                            Inventory[each] = 1
            except IndexError:
                pass
            Choices = SBImageAssembly(Data[0], Data[1])
            TempFile = discord.File(f"{FilePath}\\Files\\Images\\TEMP.png", filename="TEMP.png")
            ChoiceView = discord.ui.View()
            for each in Choices:
                if each == "Scenario":
                    pass
                else:
                    Style = self.ColorPicker(Choices, each)
                    if each == "End":
                        EndButton = discord.ui.Button(label=each,
                                    custom_id=f"{Choices['Scenario']},{Choices[each]['Destination']},{Inventory}")
                        EndButton.callback = EndButtonCallback
                        ChoiceView.add_item(EndButton)

                    elif Choices[each]['Requirement'] != "":
                        if Choices[each]['Requirement'] in Inventory:
                            if Choices[each]['Price'] != "":
                                if Choices[each]['Price'] in Inventory:

                                    ChoiceButton = discord.ui.Button(label=f"{each}  Requirement:{Choices[each]['Requirement']}  Cost:{Choices[each]['Price']}",
                                                                     custom_id=f"{Choices['Scenario']},{Choices[each]['Destination']},{Inventory},Price:{Choices[each]['Price']}",
                                                                 style=Style)
                            else:
                                ChoiceButton = discord.ui.Button(label=f"{each}"
                                                                       f" Requirement:{Choices[each]['Requirement']}",
                                                                 custom_id=f"{Choices['Scenario']},{Choices[each]['Destination']},{Inventory}",
                                                                 style=Style)
                            ChoiceButton.callback = ChoiceButtonCallback
                            ChoiceView.add_item(ChoiceButton)

                    elif Choices[each]['Price'] != "":
                        if Choices[each]['Price'] in Inventory:
                            ChoiceButton = discord.ui.Button(label=f"{each}  Cost:{Choices[each]['Price']}",
                                                             custom_id=f"{Choices['Scenario']},{Choices[each]['Destination']},{Inventory},Price:{Choices[each]['Price']}",
                                                             style=Style)
                            ChoiceButton.callback = ChoiceButtonCallback
                            ChoiceView.add_item(ChoiceButton)

                    elif Choices[each]['Reward'] != "":
                        ChoiceButton = discord.ui.Button(label=f"{each}            Reward:{Choices[each]['Reward']}",
                                                         custom_id=f"{Choices['Scenario']},{Choices[each]['Destination']},{Inventory},Reward:{Choices[each]['Reward']}",
                                                         style=Style)
                        ChoiceButton.callback = ChoiceButtonCallback
                        ChoiceView.add_item(ChoiceButton)

                    else:
                        ChoiceButton = discord.ui.Button(label=each,
                                                         custom_id=f"{Choices['Scenario']},{Choices[each]['Destination']},{Inventory}",
                                                         style=Style)
                        ChoiceButton.callback = ChoiceButtonCallback
                        ChoiceView.add_item(ChoiceButton)

            await interaction.response.edit_message(attachments=[TempFile], view=ChoiceView)

        async def SBLaunchButtonCallback(interaction):
            Data = interaction.data['custom_id'].split(",")
            Choices = SBImageAssembly(Data[0], Data[1])
            TempFile = discord.File(f"{FilePath}\\Files\\Images\\TEMP.png", filename="TEMP.png")
            SBView = discord.ui.View()
            Inventory = {}
            for each in Choices:
                if each == "Scenario":
                    pass
                else:
                    Style = self.ColorPicker(Choices,each)
                    ChoiceButton = discord.ui.Button(label=each,
                                   custom_id=f"{Choices['Scenario']},{Choices[each]['Destination']},{Inventory}",
                                   style=Style)
                    ChoiceButton.callback = ChoiceButtonCallback
                    SBView.add_item(ChoiceButton)
            await interaction.response.send_message(ephemeral=True,file=TempFile, view=SBView)

        SBLaunchButton.callback = SBLaunchButtonCallback
        View.add_item(SBLaunchButton)
        await channel.send(embed=Embed, view=View)


async def setup(bot):
    await bot.add_cog(StoryBoardDisplay(bot))
