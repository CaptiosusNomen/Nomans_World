import discord
from discord.ext import commands
import os
import sys
from TokenHolder import Token
Token = Token()



FilePath = os.path.dirname(os.path.abspath(__file__))
TOKEN = Token
intents = discord.Intents.all()
Bot = commands.Bot(command_prefix=["A*"], intents=intents, case_insensitive=True)
Bot.remove_command('help')

async def LoadCogs():
    if sys.platform == "linux" or sys.platform == "linux2":
        for file in os.listdir(f"{FilePath}/Cogs"):
            if file.endswith("Cog.py"):
                await Bot.load_extension(f'Cogs.{file[:-3]}')
                print(f"{file} Loaded")

    if sys.platform == "win32" or sys.platform == "win64":
        for file in os.listdir(f"{FilePath}\\Cogs"):
            if file.endswith("Cog.py"):
                await Bot.load_extension(f'Cogs.{file[:-3]}')
                print(f"{file} Loaded")

@Bot.event
async def on_ready():
    await LoadCogs()
    print("Bot online.")
    print(f'Client Name: {Bot.user.name}')
    print("--------------------")




@Bot.event
async def on_resumed():
    pass

Bot.run(TOKEN)
