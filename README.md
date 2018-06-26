# DiscordRP bot
Used to play Fate SRD over discord

# Set Up
in order to set up, must install python, and discord.py (discord api)
``` pip install discord ```
in the python files, a "token.txt" file must be created with ONLY the token
of the bot to be used with this code. The code will read and use the token from this file.
I have had an incidence of someone hijacking the bot
and deleting the properties of the entire channel and spamming everyone on that channel with
spam.

# Commands
The prefix can be changed by in code changing the prefix of Client(command_prefix = "!")
the default is !.

## hello
just a hello command

## cookie
sends a cookie emote

## roll
does a fudge roll, 4 dice of 3 sides, and adds them all up

## game {start|refresh|details}
starts a game, resets the game, or provides details. This is for gm use ONlY

## assign (role) <@role>
role can be one of "player" or "gm", and the @role requires a role to be mentioned
This will set the permissions of the game

## join
join the currently running game

## leave
leave the currently running game

## info <@user>
gives information of a person's character in game. the default @user is the message sender

##

## c (name) <@user>
create a new character of the name and assign it to you. the @user is optional and only usable by gm.
This is to allow the gm to help players set up

## c_add <@user> (type) (a1) (a2) (a3)
type can be of "aspect" "bar" "consequence". @user is only for gm purposes. 
multiple attributes can be added at once

## c_remove <@user> (type) (a1) (a2) (a3)
type can be of "aspect" "bar" "consequence". @user is only for gm purposes. 
multiple attributes can be removed at once
