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

## aspect (action) <@user> (args)
<@user> is only used for gm

| Action | Short | argument list | desc |
| ------ | ----- | ------------- | ---- |
| add	 | a     | (a1) (a2) (a3)  | adds aspect to a character |
| remove | r     | (a1) (a2) (a3)  | removes aspects from a character |

## skill (action) <@user> (name, level) (name, level)
<@user> is only used for gm

| Action | Short | argument list | desc |
| ------ | ----- | ------------- | ---- |
| add	 | a     | (skill) (level) (skill) (level)  | adds skill to a character |
| remove | r     | (skill) (level) (skill) (level)  | removes skills from a character |

## bar (action) <@user> (args)
<@user> is only used for gm

| Action | Short | argument list | desc |
| ------ | ----- | ------------- | ---- |
| add	 | a     | (b1) (b2)     | adds bar to a character |
| remove | r     | (b1) (b2)     | removes bar from a character |
| spend  | s     | (bar) (box) (bar) (box) | spends a box  |
| refresh| re    | (bar) (box) (bar) (box) | refreshes a box, only a gm can do so|

## fate (action) (amount) <@user>
<@user> is only used for gm
A player may only spend their points, but only a gm can give.

| Action | Short | desc |
| ------ | ----- | ---- |
| spend	 | s     |  adds fate to a character |
| give   | g     |  removes fate from a character, only a gm can give |

