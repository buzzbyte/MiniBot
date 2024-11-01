import os
import discord
from discord import Bot
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.getenv('ENV_PATH'))

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

bot = Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("MiniBot is ready")

    activity = discord.Activity(
        name="customstatus",
        state="MiniBot",
        type=discord.ActivityType.custom
    )

    await bot.change_presence(
        activity=activity,
        status=discord.Status.online
    )

@bot.command()
async def ping(ctx):
    await ctx.respond("Pong!")

bot.run(TOKEN)