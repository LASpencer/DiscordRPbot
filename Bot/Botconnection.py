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
async def c_add(context, type, player_id, *text):
    """
    Handle adding of things to characters
    :param context: context
    :param type: what are we editing of a character
    :param player_id: potential mention
    :param text: what is the text to go with it
    :return:
    """

    roles = list(role.id for role in context.message.author.roles)  # get role ids
    player = DiscordUtility.is_role(playerRole, roles)
    gm = DiscordUtility.is_role(GMRole, roles)

    game_id = get_id(context,player,gm,player_id)
    if game_id is None:
        return

    cha = game_object.get_character(game_id)
    if cha is None:
        await bot.say("no character")
        return

    #Type decoding
    type_l = type.lower()
    if type_l == "aspect":
        if player and not gm:
            cha.add_aspect(player_id) # player only refers to self, so it is an attribute
        for t in text:
            cha.add_aspect(t)
        await bot.say("aspect(s) added")
    elif type_l == "bar":
        if player and not gm:
            cha.add_bar(BarFactory.bar_default(player_id)) # player only refers to self, so it is an attribute
        for t in text:
            cha.add_bar(BarFactory.bar_default(t))
        await bot.say("bar(s) added")
    elif type_l == "consequence" or type_l == "con":
        pass

@bot.command(pass_context=True)
async def c_remove(context, type, player_id, *text):
    """
    Handle removing of attributes
    :param context: context
    :param type: what are we editing of a character
    :param player_id: potential mention
    :param text: what is the text to go with it
    :return:
    """
    roles = list(role.id for role in context.message.author.roles)  # get role ids
    player = DiscordUtility.is_role(playerRole, roles)
    gm = DiscordUtility.is_role(GMRole, roles)

    # permission
    game_id = get_id(context, player, gm, player_id)
    if game_id is None:
        return

    cha = game_object.get_character(game_id)
    if cha is None:
        await bot.say("no character")
        return

    #Type decoding
    type_l = type.lower()
    if type_l == "aspect":
        if player and not gm:
            cha.remove_aspect(player_id) # player only refers to self
        for t in text:
            cha.remove_aspect(t)
        await bot.say("aspect(s) removed")
    elif type_l == "bar":
        if player and not gm:
            cha.remove_bar(player_id) # player only refers to self
        for t in text:
            cha.remove_bar(t)
        await bot.say("bar(s) removed")
    elif type_l == "consequence" or type_l == "con":
        pass


@bot.command(pass_context=True)
async def bar(context, action, bar, box, id=None):
    """
    Do stuff with bars
    :param context: context
    :param action: spend or s, refresh or r
    :param bar: the name of the bar
    :param box: the index of the box (assume array)
    :param id: optional name for gm use
    :return:
    """
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

    a = action.lower()

    if a in ["s","spend"]:
        cha.spend_box(bar,int(box))
        await bot.say("box spent")
    elif a in ["r","refresh"]:
        if gm:  # only gm can refresh a box
            cha.refresh_box(bar, int(box))
            await bot.say("box refreshed")

@bot.command(pass_context=True)
async def fate(context, action, amount, id=None):
    """
    Do stuff with bars
    :param context: context
    :param action: spend or s, give or g
    :param amount: amount to spend or fill
    :param id: optional name for gm use
    :return:
    """
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




