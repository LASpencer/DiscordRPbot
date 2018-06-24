"""

Author : Robin Phoeng
Date : 20/06/2018
"""


import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
bot = commands.Bot(command_prefix="!")

prefix = "!"

playerRole = None
GMRole = None

@bot.event
async def on_ready():
    # will print to python console
    print("Bot is ready!")

@bot.command(pass_context=True)
async def hello(context):
    await bot.say("<@%s> hello" % context.message.author.id)

@bot.command(pass_context=False)
async def cookie():
    await bot.say(":cookie:")

@bot.command(pass_context=False)
async def roll():
    [d1,d2,d3,d4,t] = fudgeRoll()
    await bot.say("%d + %d + %d + %d = %d" % (d1,d2,d3,d4,t))

def fudgeRoll():
    d1 = random.randrange(-1, 2, 1)
    d2 = random.randrange(-1, 2, 1)
    d3 = random.randrange(-1, 2, 1)
    d4 = random.randrange(-1, 2, 1)

    return [d1,d2,d3,d4, d1+d2+d3+d4]

@bot.command(pass_context=True)
async def assign(context,role,id):
    if context.message.server.owner == context.message.author:
        if role == "player":
            global playerRole
            playerRole = id[3:len(id) - 1]
            await bot.say("player role set")
        elif role == "gm":
            global GMRole
            GMRole = id[3:len(id) - 1]
            await bot.say("gm role set")
    else:
        await bot.say("Not Owner")

@bot.event
async def on_message(message):
    global playerRole
    global GMRole
    # message.channel refers to the channel the message came from
    # await is used, as so it will wait until the bot is able to send the message, before continuing.
    if message.content.startswith(prefix):
        content = message.content[len(prefix):].lower() # remove prefix
        userID = message.author

        # admin commands
        if content.startswith("assign"):
            # only let admin do this
            # in this case, only the owner can do so
            if message.server.owner == message.author:
                args = content.split(" ") # spilt into arguments
                # we expect the format of server role, internal role

                # extract ID
                roleID = args[1][3:len(args[1])-1]
                if args[2] == "member":

                    playerRole = roleID
                if args[2] == "gm":

                    GMRole = roleID
            else:
                await bot.send_message(message.channel, "Not Owner")

        # TODO there should be a nicer way to organise code
        # code should run, 'content' then check for authentication, but this generates
        # much repeated 'verification code'.
        if content == "roll":
            [member,msg] = is_member((role.id for role in message.author.roles))
            if not member:
                await bot.send_message(message.channel, msg)
            else:
                await bot.send_message(message.channel, "Dice Roll")


        if content == "start game":
            [GM, msg] = is_GM((role.id for role in message.author.roles))
            if not GM:
                await bot.send_message(message.channel, msg)
            else:
                await bot.send_message(message.channel, "Start Game")

    await bot.process_commands(message)

async def utility(message,userID):
    if message == "hello":
        await bot.send_message(message.channel, "<@%s> hello" % userID)
    if message == "cookie":
        await bot.send_message(message.channel, ":cookie:")



def is_member(roles):
    if playerRole is None:
        return [False, "No Member Role set"]
    elif playerRole in (roles):
        return [True, "is a member"]
    else:
        return [False, "Not a Member"]

def is_GM(roles):
    if GMRole is None:
        return [False, "No GM Role set"]
    elif GMRole in (roles):
        return [True, "is a GM"]
    else:
        return [False, "Not a GM"]


bot.run("NDU4NTcwNTQ0OTkzMDA5Njgx.DgpuXg.IteIGqcCGctdKQCEUvoEExXGbjc")

