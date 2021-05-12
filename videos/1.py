import discord
import asyncio
from discord.ext import commands


# bot or client
client = commands.Bot(command_prefix=">", help_command=None)

@client.event
async def on_ready():
    print("Bot online, connected to discord!")


@client.command(name="test")
async def test(ctx):
    await ctx.channel.send("Test ran!")








client.run("TOKEN")