import discord
from discord.ext import commands
import os
import sys

FilePath = os.path.dirname(os.path.abspath(__file__))
intents = discord.Intents.all()
Bot = commands.Bot(command_prefix=["A*"], intents=intents, case_insensitive=True)
Bot.remove_command('help')

async def LoadCogs():
    if sys.platform.startswith("lin"):
        for file in os.listdir(f"{FilePath}/Cogs"):
            if file.endswith("Cog.py"):
                await Bot.load_extension(f'Cogs.{file[:-3]}')
                print(f"{file} Loaded")

    if sys.platform.startswith("win"):
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

from TokenHolder import Token
Bot.run(Token())
