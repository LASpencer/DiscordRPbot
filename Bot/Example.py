"""

Author : Robin Phoeng
Date : 20/06/2018
"""


import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix= "!")

prefix = "!"

memberRole = None
GMRole = None

@client.event
async def on_ready():
    # will print to python console
    print("Bot is ready!")

@client.event
async def on_message(message):
    global memberRole
    global GMRole
    # message.channel refers to the channel the message came from
    # await is used, as so it will wait until the client is able to send the message, before continuing.
    if message.content.startswith(prefix):
        content = message.content[len(prefix):].lower() # remove prefix
        userID = message.author
        if content == "hello":
            await client.send_message(message.channel, "<@%s> hello" % userID)
        if content == "cookie":
            await client.send_message(message.channel, ":cookie:")

        # make user-specific command
        if content == "hello admin":
            if userID == "1234123":
                await client.send_message(message.channel, "<@%s> hello" % userID)
            else:
                await client.send_message(message.channel, "No admin access")

        # make role-specific commands
        if content == "roles":
            for role in message.author.roles:
                print(role)

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

                    memberRole = roleID
                if args[2] == "gm":

                    GMRole = roleID
            else:
                await client.send_message(message.channel, "Not Owner")

        # TODO there should be a nicer way to organise code
        # code should run, 'content' then check for authentication, but this generates
        # much repeated 'verification code'.
        if content == "roll":
            [member,msg] = is_member((role.id for role in message.author.roles))
            if not member:
                await client.send_message(message.channel, msg)
            else:
                await client.send_message(message.channel, "Dice Roll")


        if content == "start game":
            [GM, msg] = is_GM((role.id for role in message.author.roles))
            if not GM:
                await client.send_message(message.channel, msg)
            else:
                await client.send_message(message.channel, "Start Game")

def is_member(roles):
    if memberRole is None:
        return [False, "No Member Role set"]
    elif memberRole in (roles):
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


client.run("NDU4NTcwNTQ0OTkzMDA5Njgx.DgpuXg.IteIGqcCGctdKQCEUvoEExXGbjc")

