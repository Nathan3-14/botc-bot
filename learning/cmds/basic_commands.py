import discord
from discord.ext import commands
from discord.ext.commands.context import Context as CTX

@commands.group(aliases=["bc"])
async def basic_commands(ctx: CTX):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"{ctx.subcommand_passed} does not exist under basic_commands")

@basic_commands.command()
async def ping(ctx: CTX):
    """ Answers with Pong"""
    
    await ctx.send("pong")

@basic_commands.command()
async def welcome(ctx: CTX, new_person: discord.Member):
    """Welcomes people"""
    
    await ctx.send(f"Welcome {new_person.name}!\n:)")

async def setup(bot):
    bot.add_command(basic_commands)
