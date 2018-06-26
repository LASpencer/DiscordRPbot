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


"""
####################################################################
Utility Functions
####################################################################
"""
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


"""
####################################################################
Discord Set up
####################################################################
"""
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


"""
####################################################################
Game Set up
####################################################################
"""
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
        if game_object.add_player(context.message.author.id):
            await bot.say("Joined game")

@bot.command(pass_context=True)
async def leave(context):
    roles = list(role.id for role in context.message.author.roles)  # get role ids
    if is_gm(roles) or is_player(roles):
        global game_object
        if game_object.remove_player(context.message.author.id):
            await bot.say("left game")

@bot.command(pass_context=True)
async def c(context,name,id=None):
    roles = list(role.id for role in context.message.author.roles)  # get role ids
    player = is_player(roles)
    gm = is_gm(roles)

    if not player and not gm:
        return

    if id is None and gm:
        bot.say("No player")
        return

    if id is None and player:
        game_id = context.message.author.id
    else:
        game_id = id[2:len(id) - 1] #TODO add some verification of id format.

    game_object.new_character(name,game_id)
    await bot.say("character added")

"""
####################################################################
Game Utility
####################################################################
"""
@bot.command(pass_context=True)
async def info(context, id=None):

    if id is None:
        game_id = context.message.author.id
    else:
        game_id = id[2:len(id) - 1] #TODO add some verification of id format.

    cha = game_object.get_character(game_id)
    if cha is None:
        await bot.say("no character")
    else:
        await bot.say(str(cha))

"""
####################################################################
Game Play
####################################################################
"""

@bot.command(pass_context=True)
async def c_add(context, type : str,player_id: discord.Member = None, *text):
    """
    Handle adding of things to characters
    :param context: context
    :param type: what are we editing of a character
    :param text: what is the text to go with it
    :param player_id: mention
    :return:
    """
    roles = list(role.id for role in context.message.author.roles)  # get role ids
    player = is_player(roles)
    gm = is_gm(roles)

    if not player and not gm:
        return

    if gm:
        if id is None:
            print(id)
            await bot.say("no player targeted")
            return
        else:
            game_id = player_id.id
    else:
        game_id = context.message.author.id

    cha = game_object.get_character(game_id)
    if cha is None:
        bot.say("no character")
        return

    #Type decoding
    type_l = type.lower()
    if type_l == "aspect":
        for t in text:
            cha.add_aspect(t)
        pass
    elif type_l == "bar":
        cha.add_bar(text)
        pass
    elif type_l == "consequence" or type_l == "con":
        pass

@bot.command(pass_context=True)
async def c_remove(context, type, *text, id= None):
    """
    Handle all the comment
    :param context: context
    :param type: what are we editing of a character
    :param text: what is the text to go with it
    :param id: optional id
    :return:
    """
    roles = list(role.id for role in context.message.author.roles)  # get role ids
    player = is_player(roles)
    gm = is_gm(roles)

    if not player and not gm:
        return

    if gm:
        if id is None:
            await bot.say("no player targeted")
            return
        else:
            game_id = id[2:len(id) - 1]  # TODO add some verification of id format.
    else:
        game_id = context.message.author.id

    cha = game_object.get_character(game_id)
    if cha is None:
        bot.say("no character")
        return

    #Type decoding
    type_l = type.lower()
    if type_l == "aspect":
        for t in text:
            cha.remove_aspect(t)
        pass
    elif type_l == "bar":
        pass
    elif type_l == "consequence" or type_l == "con":
        pass

@bot.event
async def on_message(message):
    await bot.process_commands(message)

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


"""
Read token from file, which is git-ignored to prevent stolen bot
file should just have token in it.
"""
with open("token.txt","r") as file:
    token = file.read()

bot.run(token)

