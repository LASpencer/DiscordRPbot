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
import DiscordUtility
import BarFactory

Client = discord.Client()
bot = commands.Bot(command_prefix="!")

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
    [d1,d2,d3,d4,t] = DiscordUtility.fudgeRoll()
    await bot.say("%d + %d + %d + %d = %d" % (d1,d2,d3,d4,t))

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
            role_id = DiscordUtility.valid_role(id)
            if role_id is not None:
                playerRole = role_id
                await bot.say("player role set")
            else:
                await bot.say("not a valid role")
        elif role == "gm":
            global GMRole
            role_id = DiscordUtility.valid_role(id)
            if role_id is not None:
                GMRole = role_id
                await bot.say("GM role set")
            else:
                await bot.say("not a valid role")
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
    if DiscordUtility.is_role(GMRole,roles):
        if arg == "start":
            await bot.say("Start Game")
        if arg == "refresh":
            await bot.say("refresh Game")
        if arg == "details":
            await bot.say(str(game_object))
    else:
        await bot.say("Not GM")

@bot.command(pass_context=True)
async def c(context,name,id=None):
    roles = list(role.id for role in context.message.author.roles)  # get role ids
    player = DiscordUtility.is_role(playerRole, roles)
    gm = DiscordUtility.is_role(GMRole, roles)

    game_id = get_id(context, player, gm, id)
    if game_id is None:
        return

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
        game_id = DiscordUtility.valid_id(id)
        if game_id is None:
            await bot.say("no player targeted")
            return

    cha = game_object.get_character(game_id)
    if cha is None:
        await bot.say("no character")
    else:
        await bot.say(str(cha))

@bot.command(pass_context=True)
async def info_fate(context, id=None):
    roles = list(role.id for role in context.message.author.roles)  # get role ids
    player = DiscordUtility.is_role(playerRole, roles)
    gm = DiscordUtility.is_role(GMRole, roles)

    game_id = get_id(context, player, gm, id)
    if game_id is None:
        return

    cha = game_object.get_character(game_id)
    if cha is None:
        await bot.say("no character")
        return

    await bot.send_message(context.message.author,"%s has %d fate points" % (cha.get_name(),cha.get_fate()))

"""
####################################################################
Game Play
####################################################################
"""

@bot.command(pass_context=True)
async def aspect(context, action, player_id, *text):
    """
    Handles aspect addition and removal
    :param context: context of message
    :param action: one of [add, a] or [remove, r]
    :param player_id: optional player id, for gm use only
    :param text: the list of aspects to add
    """
    header = gm_player_command_header(context, player_id, text)
    if header is None:
        return
    [player, gm, cha, args] = header

    a = action.lower() # non-case sensitive

    if a in ["add", "a"]:
        for t in args:
            cha.add_aspect(t)
        await bot.say("aspect(s) added")
    elif a in ["remove","r"]:
        for t in args:
            cha.remove_aspect(t)
        await bot.say("aspect(s) removed")

@bot.command(pass_context=True)
async def skill(context,action, player_id,*text):
    """
    handle addition and removal of skills
    :param context: context
    :param action: either [add,a] or [remove,r]
    :param player_id: optional id for gm use
    :param text: the list of arguments
    """
    header = gm_player_command_header(context,player_id,text)
    if header is None:
        return
    [player, gm, cha, args] = header

    a = action.lower()  # non-case sensitive

    if a in ["add", "a"]:
        pairs = zip(args[0::2],args[1::2])
        # each pair goes (name, level)
        for p in pairs:
            # TODO check that the order is in pairs
            cha.add_skill(int(p[1]),p[0])
        await bot.say("skill(s) added")
    elif a in ["remove", "r"]:
        for t in args:
            cha.remove_skill(t)  # player only refers to self
        await bot.say("skill(s) removed")

@bot.command(pass_context=True)
async def bar(context, action, id, *text):
    """
    Do stuff with bars
    :param context: context
    :param action: one of [spend, s] [refresh,r] [add,a] [remove r]
    :param id: optional name for gm use
    :param text: list of arguments
    :return:
    """
    header = gm_player_command_header(context, id, text)
    if header is None:
        return
    [player, gm, cha, args] = header

    a = action.lower()

    if a in ["s","spend"]:
        pairs = zip(args[0::2], args[1::2])  # generate pairs
        # must be in pairs of 2, going box, bar
        for p in pairs:
            cha.spend_box(p[0],int(p[1]))
        await bot.say("box(s) spent")
    elif a in ["re","refresh"]:
        if gm:  # only gm can refresh a box
            pairs = zip(args[::2], args[1::2])  # generate pairs
            for p in pairs:
                cha.refresh_box(p[0], int(p[1]))
            await bot.say("box(s) refreshed")
    elif a in ["add","a"]:
        for t in args:
            cha.add_bar(BarFactory.bar_default(t))
        await bot.say("box(s) added")
    elif a in ["remove","r"]:
        for t in args:
            cha.remove_bar(t)
        await bot.say("bar(s) removed")

@bot.command(pass_context=True)
async def fate(context, action, amount, id=None):
    """
    Do stuff with bars
    :param context: context
    :param action: spend or s, give or g
    :param amount: amount to spend or fill
    :param id: optional name for gm use
    """
    #TODO this code process an argument list unnecessarily
    header = gm_player_command_header(context, id, ())
    if header is None:
        return
    [player, gm, cha, args] = header

    a = action.lower()

    if a in ["s","spend"]:
        cha.change_fate(-int(amount))
        await bot.say("%s fate spent" % amount)
    elif a in ["g","give"]:
        if gm:  # only gm can refresh a box
            cha.change_fate(int(amount))
            await bot.say("%s fate given" % amount)


@bot.event
async def on_message(message):
    await bot.process_commands(message)

def gm_player_command_header(context,id,text):
    """
    Sorts out player and gm commands
    :param context: context of message
    :param id: optional id entered (may not be id)
    :param text: the list of arguments as a tuple
    :return: player : boolean, gm : boolean, character : Character, args : list
    """
    roles = list(role.id for role in context.message.author.roles)  # get role ids
    player = DiscordUtility.is_role(playerRole, roles)
    gm = DiscordUtility.is_role(GMRole, roles)

    game_id = get_id(context, player, gm, id)
    if game_id is None:
        return None # end command

    cha = game_object.get_character(game_id)
    if cha is None:
        bot.say("no character")
        return None # end command

    args = list(text)

    if player and not gm:
        args.insert(0,id)  # add id

    return [player,gm,cha,args]


def get_id(context,player,gm,id):
    """
    short hand of some code.
    a gm MUST specify an ID, while a player does not and cannot
    :param context: the context of the message
    :param player: player boolean
    :param gm: gm boolean
    :param id: id argument
    :return: id if possible, otherwise None
    """

    if not player and not gm:
        return None

    if gm:
        game_id = DiscordUtility.valid_id(id)
        if game_id is None:
            bot.say("no player targeted")
            return None
    else:
        game_id = context.message.author.id
    return game_id



"""
Read token from file, which is git-ignored to prevent stolen bot
file should just have token in it.
"""
with open("token.txt", "r") as file:
    token = file.read()

bot.run(token)




