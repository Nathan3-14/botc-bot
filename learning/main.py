from dotenv import load_dotenv
import os
from rich.console import Console
import pathlib
import discord
from discord.ext import commands
from discord.ext.commands.context import Context as CTX
# from cogs.greetings import Greetings

#* Load from dotenv *#
load_dotenv()
temp_token = os.getenv("TOKEN")
token = temp_token if temp_token is not None else ""
intents = discord.Intents.default()
intents.message_content = True

#* Load Commands *#
base_dir = pathlib.Path(__file__).parent
cmd_dir = base_dir / "cmds"

#* Setup other Variables *#
error_messages = {
    commands.MissingRequiredArgument: "Missing required argument",
    commands.CommandNotFound: "Incorrect command name"
}
console = Console()
pprint = console.print

#* Run Command *#
def run():
    bot = commands.Bot(command_prefix="?", intents=intents)

    @bot.event
    async def on_ready() -> None:
        pprint(f"[light_green bold]Logged in as {bot.user}[/light_green bold]")
        pprint(f"[light_green bold]Setting up Commands in[/light_green bold] [cyan]{cmd_dir}[/cyan]")

        for command_file in cmd_dir.glob("*.py"):
            if command_file.name == "__init__.py":
                continue
            await bot.load_extension(f"cmds.{command_file.name[:-3]}")
            pprint(f"[light_green bold]Loaded[/light_green bold] [cyan]{command_file.name}[/cyan]")
        
        pprint("[light_green bold]Commands set up successfully[/light_green bold]")
    
    @bot.event
    async def on_command_error(ctx: CTX, error):
        error_type = type(error)
        message = error_messages[error_type] if error_type in list(error_messages.keys()) else "silly error D:\ncontact devloper plz :)"
        await ctx.send(message)

    
    
    bot.run(token=token)

if __name__ == "__main__":
    run()
