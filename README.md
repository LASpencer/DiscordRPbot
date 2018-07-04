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
starts a game, resets the game, or provides details. This is for gm use only

## load (type)
loads to a file
| Action | Short | argument list | desc |
| ------ | ----- | ------------- | ---- |
| roles  | r     | None          | loads the gm and player role from roles.txt |

## save (type)
saves to a file
| Action | Short | argument list | desc |
| ------ | ----- | ------------- | ---- |
| roles  | r     | None          | saves the gm and player role to roles.txt |

## assign (role) <@role>
role can be one of "player" or "gm", and the @role requires a role to be mentioned
This will set the permissions of the game

## info <@user>
gives information of a person's character in game. the default @user is the message sender.
A character can be addressed by their name, or if it is a player, by a mention.

## character <@user> (name)
short form is "!c <@user> (name)"
create a new character of the name and assign it to you. the @user is optional and only usable by gm.
This is to allow the gm to help players set up

## object (name)
short form is "!o (name)"
only usable by gm
Creates a new game character.

## aspect (action) <name> (args)
<name> is only used for gm. it can be a mention, or name of character

| Action | Short | argument list | desc |
| ------ | ----- | ------------- | ---- |
| add	 | a     | (a1) (a2) (a3)  | adds aspect to a character |
| remove | r     | (a1) (a2) (a3)  | removes aspects from a character |

## skill (action) <name> (name, level) (name, level)
<name> is only used for gm. it can be a mention, or name of character

| Action | Short | argument list | desc |
| ------ | ----- | ------------- | ---- |
| add	 | a     | (skill) (level) (skill) (level)  | adds skill to a character |
| remove | r     | (skill) (level) (skill) (level)  | removes skills from a character |


## bar (action) <name> (args)
<name> is only used for gm. it can be a mention, or name of character

| Action | Short | argument list | desc |
| ------ | ----- | ------------- | ---- |
| add	 | a     | (b1) (b2)     | adds bar to a character |
| remove | r     | (b1) (b2)     | removes bar from a character |
| spend  | s     | (b1) (b2)     | spends a bar  |
| refresh| re    | (b1) (b2)     | refreshes a bar, only a gm can do so|

## box (action) <name> (args)
<name> is only used for gm. it can be a mention, or name of character

| Action | Short | argument list | desc |
| ------ | ----- | ------------- | ---- |
| add	 | a     | (bar) (size) (bar) (size)  | adds bar to a character at the end |
| remove | r     | (bar) (index) (bar) (index) | removes bar from a character. Note: *remove bar 1 bar 1* will remove boxes at index 1 and 2|
| spend  | s     | (bar) (box) (bar) (box) | spends a box  |
| refresh| re    | (bar) (box) (bar) (box) | refreshes a box, only a gm can do so|

## consequence (action) (modifier) <name> (args)
it can also be added as cons (shortcut)
<name> is only used for gm. it can be a mention, or name of character

| Action | Short | argument list | desc |
| ------ | ----- | ------------- | ---- |
| add	 | a     | (name) optional | adds a consequence to a modifier|
| remove | r     | none          | removes a consequence, gm only|
| info   | i     | none          | information about a consequence|
| aspectadd | aa | (a1) (a2)     | add aspects to consequence|
| aspectremove|ar| (a1) (a2)     | remove aspects of consequence, gm only|
| text   | t     | (a1) only takes first | sets flavour set of consequence|

## fate (action) <name> (amount) 
<name> is only used for gm. it can be a mention, or name of character
A player may only spend their points, but only a gm can give.

| Action | Short | desc |
| ------ | ----- | ---- |
| spend	 | s     |  adds fate to a character |
| give   | g     |  removes fate from a character, only a gm can give |

