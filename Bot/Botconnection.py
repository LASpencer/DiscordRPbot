"""

Author : Robin Phoeng
Date : 19/06/2018
"""


import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix= "!")


@client.event
async def on_ready():
    # will print to python console
    print("Bot is ready!")

@client.event
async def on_message(message):
    # message.channel refers to the channel the message came from
    # await is used, as so it will wait until the client is able to send the message, before continuing.
    if message.content == "hello":
        await client.send_message(message.channel,"hello there")

client.run("NDU4NTcwNTQ0OTkzMDA5Njgx.DgpuXg.IteIGqcCGctdKQCEUvoEExXGbjc")

