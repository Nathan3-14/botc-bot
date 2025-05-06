import datetime
from typing import Any, Dict, Literal
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from discord.ext.commands.context import Context as CTX
import settings

from rich.console import Console

console = Console()
TIME = settings.colours["time"]
INFO = settings.colours["info"]
WARNING = settings.colours["warning"]
ERROR = settings.colours["error"]
ERROR_TEXT = settings.colours["error_text"]
IMPORTANT = settings.colours["important"]


def log(message: str, type: Literal["info", "warning", "error", "important"]="info") -> None:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%y-%m-%d")
    match type:
        case "info":
            log_output = f"{current_time} INFO {message}"
            text_output = f"[{TIME}]{current_time}[/{TIME}] [{INFO} bold]INFO[/{INFO} bold] {message}"
        case "warning":
            log_output = f"{current_time} WARNING {message}"
            text_output = f"[{TIME}]{current_time}[/{TIME}] [{WARNING} bold]WARNING[/{WARNING} bold] {message}"
        case "error":
            log_output = f"{current_time} ERROR {message}"
            text_output = f"[{TIME}]{current_time}[/{TIME}] [{ERROR} bold]ERROR[/{ERROR} bold] [{ERROR_TEXT} bold]{message}[/{ERROR_TEXT} bold]"
        case "important":
            log_output = f"{current_time} IMPORTANT {message}"
            text_output = f"[{TIME}]{current_time}[/{TIME}] [{IMPORTANT} bold]IMPORTANT[/{IMPORTANT} bold] [bold]{message}[/bold]"
    
    console.print(text_output)
    with open(f"{settings.LOGS_DIR}/{current_date}.log", "a") as f:
        f.write(log_output + "\n")



def main() -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix="?", intents=intents)
    
    @bot.event
    async def on_ready():
        log("Bot Logged in Successfully")
    
    @bot.command()
    async def sync(ctx: CTX) -> None:
        guild = discord.Object(id=1342227524129652780)
        ctx.bot.tree.copy_global_to(guild=guild)
        await ctx.bot.tree.sync(guild=guild)

        log("Synced slash commands", "important")
        await ctx.send("Sync Successful!")
    
    @bot.hybrid_command()
    async def ping(interaction: CTX):
        await interaction.send("Pong!")
    
    
    if settings.token is None:
        log("No bot token provided", "error")
        return
    print(settings.token)
    bot.run(settings.token)

if __name__ == "__main__":
    # log("Hello!")
    # log("Warn test?", "warning")
    # log("err :(", "error")
    # log("SUPER IMPORTANT THING", "important")
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        log("Shutting down bot...")
        log("Goodbye! :)", "important")
        log("")
        

