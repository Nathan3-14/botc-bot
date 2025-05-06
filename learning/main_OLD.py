from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from discord.ext.commands.context import Context as CTX

#* Load from dotenv *#
load_dotenv()
temp_token = os.getenv("TOKEN")
token = temp_token if temp_token is not None else ""
intents = discord.Intents.default()
intents.message_content = True

error_messages = {
    commands.MissingRequiredArgument: "Missing required argument",
    commands.CommandNotFound: "Incorrect command name"
}

def run():
    bot = commands.Bot(command_prefix="?", intents=intents)

    @bot.event
    async def on_ready() -> None:
        print(bot.user)
    
    @bot.event
    async def on_command_error(ctx: CTX, error):
        # match type(error):
        #     case commands.MissingRequiredArgument:
        #         message =  ""
        # if isinstance(error, commands.MissingRequiredArgument):
        #     await ctx.send("Error happened ):")
        
        error_type = type(error)
        message = error_messages[error_type] if error_type in list(error_messages.keys()) else "silly error D:\ncontact devloper plz :)"
        await ctx.send(message)
    
    
    
    @bot.group(aliases=["bc"])
    async def basic_commands(ctx: CTX):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"{ctx.subcommand_passed} does not exist under basic_commands")
    
    @basic_commands.command()
        # aliases=["p"],
        # help="Answers with Pong",
        # description="Simple test Command",
        # brief="Answers with Pong",
        # enabled=False
    async def ping(ctx: CTX):
        """ Answers with Pong"""
        
        await ctx.send("pong")
    
    @basic_commands.command()
    async def welcome(ctx: CTX, new_person: discord.Member):
        """Welcomes people"""
        
        await ctx.send(f"Welcome {new_person.name}!\n:)")
    
    
    bot.run(token=token)

if __name__ == "__main__":
    run()
