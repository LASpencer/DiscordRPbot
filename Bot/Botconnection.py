"""

Author : Robin Phoeng
Date : 24/06/2018
"""


import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from Game import Game

Client = discord.Client()
bot = commands.Bot(command_prefix="!")

prefix = "!"

playerRole = None
GMRole = None
game_object = Game()


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
async def assign(context,role_arg,id):
    if context.message.server.owner == context.message.author:
        role = role_arg.lower() # non-case-sensitive
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

@bot.command(pass_context=True)
async def game(context,arg):
    roles = list(role.id for role in context.message.author.roles) # get role ids
    if is_gm(roles):
        if arg == "start":
            await bot.say("Start Game")
        if arg == "refresh":
            await bot.say("refresh Game")
        if arg == "details":
            await bot.say(str(game_object))
    else:
        await bot.say("Not GM")

@bot.command(pass_context=True)
async def join(context):
    roles = list(role.id for role in context.message.author.roles) # get role ids
    if is_gm(roles) or is_player(roles):
        global game_object
        game_object.add_player(context.message.author.id)
        await bot.say("Joined game")



@bot.event
async def on_message(message):
    await bot.process_commands(message)

async def utility(message,userID):
    if message == "hello":
        await bot.send_message(message.channel, "<@%s> hello" % userID)
    if message == "cookie":
        await bot.send_message(message.channel, ":cookie:")

def is_player(roles):
    global playerRole
    if playerRole is None:
        return False
    elif playerRole in roles:
        return True
    else:
        return False

def is_gm(roles):
    global GMRole
    if GMRole is None:
        return False
    elif GMRole in roles:
        return True
    else:
        return False


bot.run("NDU4NTcwNTQ0OTkzMDA5Njgx.DgpuXg.IteIGqcCGctdKQCEUvoEExXGbjc")

