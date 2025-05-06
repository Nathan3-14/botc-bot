import discord
from discord.ext import commands
from discord.ext.commands.context import Context as CTX

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx: CTX, *, member: discord.Member):
        await ctx.send(f"Hello to {member.name}!")

async def setup(bot):
    await bot.add_cog(Greetings)
