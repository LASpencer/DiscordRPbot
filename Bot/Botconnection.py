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
from Bar import Box

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
async def roll(*list):
    """
    handles rolls on advantages
    :param list: list of potential numbers
    """
    advantages = []
    for i in list:
        try:
            advantages.append(int(i))
        except ValueError:
            await bot.say("%s is not a valid integer" % i)
            return

    [d1,d2,d3,d4,t] = DiscordUtility.fudgeRoll()

    output = "```\nroll  : %d + %d + %d + %d = %d" % (d1,d2,d3,d4,t)
    output += "\ntotal : %d" % t  # add total to new line
    for i in advantages:
        output += " + %d" % i
        t += i
    # add total at the end
    output += " = %d\n```" % t

    await bot.say(output)

"""
####################################################################
Discord Set up
####################################################################
"""
@bot.command(pass_context=True)
async def assign(context,role_arg,id):

    if context.message.server.owner != context.message.author:
        await not_owner_message()
        return
    role = role_arg.lower() # non-case-sensitive
    if role in ["p", "player", "gm", "gamemaster"]:
        role_id = DiscordUtility.valid_role(id)
        if role_id is None:
            await bot.say("not a valid role")
            return

        if role in ["p","player"]:
            global playerRole
            playerRole = role_id
            await bot.say("player role set")
        else:
            global GMRole
            GMRole = role_id
            await bot.say("GM role set")
    else:
        await bot.say("assign role of(p)layer or gamemaster(gm)")


@bot.command(pass_context=True)
async def load(context,action,*args):
    if context.message.server.owner != context.message.author:
        await not_owner_message()
        return
    a = action.lower()

    if a in ["roles", "r"]:
        with open("Game/roles.txt","r") as text:
            roles = text.read().split("\n")
            global playerRole
            global GMRole
            playerRole = roles[0]
            GMRole = roles[1]
        await bot.say("roles loaded")


@bot.command(pass_context=True)
async def save(context,action, *args):
    if context.message.server.owner != context.message.author:
        await not_owner_message()
        return
    a = action.lower()

    if a in ["roles","r"]:
        with open("Game/roles.txt","w") as roles:
            global playerRole
            global GMRole
            roles.write(playerRole + "\n")
            roles.write(GMRole)
        await bot.say("roles saved")



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
            game_object.refresh()
            await bot.say("refresh Game")
        if arg == "details":
            await bot.say(str(game_object))
    else:
        await not_gm_message()

@bot.command(pass_context=True)
async def c(context, a1, a2=None):
    await new_character(context,a1,a2)

@bot.command(pass_context=True)
async def character(context,a1,a2=None):
    await new_character(context,a1,a2)

async def new_character(context,a1, a2=None):
    """
    make a new character
    :param context: context
    :param a1: id, could also be name
    :param a2: name
    """
    roles = list(role.id for role in context.message.author.roles)  # get role ids
    player = DiscordUtility.is_role(playerRole, roles)
    gm = DiscordUtility.is_role(GMRole, roles)

    if not player and not gm:
        return None

    if gm:
        game_id = DiscordUtility.valid_id(a1)
        if game_id is None: # not a valid mention, test for name
            await bot.say("no user targeted")
            return
    else:
        game_id = context.message.author.id

    if gm:
        name = a2
    else:
        name = a1

    if game_object.player_link_character(name, game_id):
        await bot.say("character linked")
    else:
        await bot.say("character added")

@bot.command(pass_context=True)
async def o(context, *names):
    await new_object(context,names)

@bot.command(pass_context=True)
async def object(context,*names):
    await new_object(context,names)

async def new_object(context,names):
    """
    make a new character
    :param context: context
    :param name: tuples
    """
    roles = list(role.id for role in context.message.author.roles)  # get role ids
    gm = DiscordUtility.is_role(GMRole, roles)
    if gm:
        for name in names:
            game_object.new_character(name)
        await bot.say("character added")
    else:
        await not_gm_message()

"""
####################################################################
Game Utility
####################################################################
"""
@bot.command(pass_context=True)
async def info(context, arg=None):
    """
    Gets information of a character
    :param context: context
    :param arg: can be an id, or name
    """

    if arg is None:
        name = context.message.author.id
    else:
        name = DiscordUtility.valid_id(arg)
        if name is None:  # not a valid mention, test for name
            name = arg.lower()

    cha = game_object.get_character(name)
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
async def aspect(context, action, player_id, *text):
    """
    Handles aspect addition and removal
    :param context: context of message
    :param action: one of [add, a] or [remove, r]
    :param player_id: optional player id, for gm use only
    :param text: the list of aspects to add
    """
    header = await gm_player_command_header(context, player_id, text)
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
    header = await gm_player_command_header(context,player_id,text)
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
    header = await gm_player_command_header(context, id, text)
    if header is None:
        return
    [player, gm, cha, args] = header

    a = action.lower()

    if a in ["s","spend"]:
        for t in args:
            cha.spend_bar(t)
        await bot.say("bar(s) spent")
    elif a in ["re","refresh"]:
        if gm:  # only gm can refresh a bar
            for t in args:
                cha.refresh_bar(t)
            await bot.say("bar(s) refreshed")
        else:
            await not_gm_message()
    elif a in ["add","a"]:
        for t in args:
            cha.add_bar(BarFactory.bar_default(t))
        await bot.say("bar(s) added")
    elif a in ["remove","r"]:
        for t in args:
            cha.remove_bar(t)
        await bot.say("bar(s) removed")

@bot.command(pass_context=True)
async def box(context, action, id, *text):
    """
    Handle box addition, removal
    for removal, it will do it in order of removal.
    If you call remove[0] remove[0] it will remove boxes 0 and 1.
    as 1 shifted into place.
    :param context: context
    :param action: one of [remove,r] or [add,a]
    :param id: optional id for gm
    :param text: tuple of arguments
    """
    header = await gm_player_command_header(context, id, text)
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
        else:
            await not_gm_message()
    elif a in ["add","a"]:
        pairs = zip(args[0::2], args[1::2])  # generate pairs
        for p in pairs:
            bar = cha.get_bar(p[0])
            if bar is None:
                continue
            bar.add_box(Box(int(p[1])))
        await bot.say("box(s) added")
    elif a in ["remove", "r"]:
        pairs = zip(args[0::2], args[1::2])  # generate pairs
        for p in pairs:
            bar = cha.get_bar(p[0])
            if bar is None:
                continue
            bar.remove_box(Box(int(p[1])))
        await bot.say("box(s) removed")

@bot.command(pass_context=True)
async def consequence(context, action, modifier, id=None, *text):
    await consequence_code(context,action,modifier,id,text)

@bot.command(pass_context=True) # shortcut for consequence
async def cons(context, action, modifier, id=None, *text):
    await consequence_code(context,action,modifier,id,text)

async def consequence_code(context, action, modifier, id=None, *text):
    """
    Do stuff with barsa
    :param context: context
    :param action: one of [spend, s] [refresh,r] [add,a] [remove r]
    :param id: optional name for gm use
    :param modifier: the consequence we are affecting
    :param text: list of arguments
    :return:
    """
    header = await gm_player_command_header(context, id, text)
    if header is None:
        return
    [player, gm, cha, args] = header

    m = await positive_num(modifier)

    a = action.lower()

    if a in ["add","a"]:
        cha.add_consequence(m)
        await bot.say("consequence added")
    elif a in ["remove","r"]:
        if gm:
            cha.remove_consequence(m)
            await bot.say("consequence removed")
        else:
            await not_gm_message()
    elif a in ["info","i"]:
        cons = cha.get_consequence(m)
        await bot.say(str(cons))
    elif a in ["text","t"]:
        cons = cha.get_consequence(m)
        cons.set_text(args[0]) # take only the first argument
        await bot.say("consequence text changed")
    elif a in ["aa","aspectadd"]:
        cons = cha.get_consequence(m)
        for t in args:
            cons.add_aspect(t)
        await bot.say("consequence aspect(s) added")
    elif a in ["ar","aspectremove"]:
        if gm:
            cons = cha.get_consequence(m)
            for t in args:
                cons.remove_aspect(t)
            await bot.say("consequence aspect(s) removed")
        else:
            await not_gm_message()



@bot.command(pass_context=True)
async def fate(context, action, id=None, *args):
    """
    Do stuff with bars
    :param context: context
    :param action: spend or s, give or g
    :param id : optional id
    :param args: list of arguments
    """
    header = await gm_player_command_header(context, id, args)
    if header is None:
        return
    [player, gm, cha, args] = header

    a = action.lower()

    if a in ["s","spend"]:
        amount = await positive_num(args[0])
        if amount is not None and cha.change_fate(-amount):
            await bot.say("%s fate spent" % amount)
        else:
            await bot.say("not enough fate points")
    elif a in ["g", "give"]:
        if gm:
            amount = await positive_num(args[0])
            if amount is not None and cha.change_fate(amount):
                await bot.say("%s fate given" % amount)
            else:
                await bot.say("exceed maximum fate points")
        else:
            await not_gm_message()
    elif a in ["i","info"]:
        await bot.send_message(context.message.author, "%s has %d fate points" % (cha.get_name(), cha.get_fate()))
    elif a in ["rset","refreshSet"]:
        if gm: # GM only action
            amount = await positive_num(args[0])
            cha.set_refresh_fate(amount)
            await bot.say("character refresh set to %d" % amount)
        else:
            await not_gm_message()



async def positive_num(num):
    """
    check a number is an non-negative integer.
    :param num: string to be check
    :return: None if invalid, integer if valid
    """
    try:
        amount = int(num)
    except ValueError:
        await bot.say("not valid amount")
        return None

    if amount <= 0:
        await bot.say("cannot be 0 or negative")
        return None

    return amount

@bot.event
async def on_message(message):
    await bot.process_commands(message)

async def gm_player_command_header(context,id,text):
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

    if not player and not gm:
        return None

    if gm:
        game_id = DiscordUtility.valid_id(id)
        if game_id is None: # not a valid mention, test for name
            game_id = id.lower()
    else:
        game_id = context.message.author.id

    if game_id is None:
        return None # end command

    cha = game_object.get_character(game_id)
    if cha is None:
        await bot.say("no character targeted")
        return None # end command

    args = list(text)

    if player and not gm:
        args.insert(0,id)  # add id

    return [player,gm,cha,args]


async def not_gm_message():
    """
    sends a not gm message, used to reduce connascence
    """
    await bot.say("not gm")

async def not_owner_message():
    """
    send a not owner message, used to reduce connascence
    :return:
    """
    await bot.say("not owner")
"""
Read token from file, which is git-ignored to prevent stolen bot
file should just have token in it.
"""
with open("token.txt", "r") as file:
    token = file.read()

bot.run(token)




