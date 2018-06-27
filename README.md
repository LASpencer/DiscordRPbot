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

## info <@user>
gives information of a person's character in game. the default @user is the message sender

## info_fate <@user>
private messages the number of fate points. A player can only see their own, while a gm 
can use the additional @user parameter to look at everyones

## c (name) <@user>
create a new character of the name and assign it to you. the @user is optional and only usable by gm.
This is to allow the gm to help players set up

## c_add <@user> (type) (a1) (a2) (a3)
type can be of "aspect" "bar" "consequence". @user is only for gm purposes. 
multiple attributes can be added at once

## c_remove <@user> (type) (a1) (a2) (a3)
type can be of "aspect" "bar" "consequence". @user is only for gm purposes. 
multiple attributes can be removed at once

## bar (action) (bar) (box) <@user>
action can be one of spend or refresh. s and r are short forms. The bar is the name while box is the index.
The @user is for gm only.
## fate (action) (amount) <@user>
action can be spend or give. s and g are short forms. Only a player may spend their own points, 
while a gm can give and spend, but need to specify user


