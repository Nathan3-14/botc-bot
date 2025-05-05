import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from rich.console import Console

console = Console()

#* Environment Setup *#
load_dotenv()
temp_token = os.getenv("TOKEN")
token = temp_token if temp_token != None else ""

#* Bot Setup *#
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="?", intents=intents)

