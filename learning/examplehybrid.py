import discord
from discord.ext import commands
    

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event 
async def on_ready():
    print("logged in yk")

@bot.command()
async def sync(ctx: commands.Context) -> None:
    guild = discord.Object(id=1342227524129652780)
    ctx.bot.tree.copy_global_to(guild=guild)
    await ctx.bot.tree.sync(guild=guild)

    print("synced")
    await ctx.send("Synced")


@bot.hybrid_command()
async def ping(ctx: commands.Context) -> None:  # This is a hybrid command, it can be used as a slash command and as a normal command
    await ctx.send(f"> Pong! {round(bot.latency * 1000)}ms")
    
# @bot.tree.command()
# async def ciao(interaction: discord.Interaction):
#     await interaction.response.send_message(f"Ciao! {interaction.user.mention}", ephemeral=True)
    
bot.run("MTM2ODg2NzEwNTQ0MDY2NTcwMA.Gde941.hjLGGefvLl3dkBOm-OSLC0PmNOxg9ewplFmOug")
