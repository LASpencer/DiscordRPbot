# Basics

## Dice roll
Fudge dice roller, 3-sided dice (-1,0,1)
Rolls 4 times and returns sum.

- Can use a discrete distribution, and one random function call to improve speed

## Aspects
Aspects are tied to characters, can be **invoked** and **compelled**
There can also be situation(temporary) and global aspects.

## Fate Points
Fate points are the currency for game influence. Needs to be tracked. 
- Refresh: when new session starts, if the player's FP < Refresh, set FP to Refresh
- Players gains FP for accepting compels, and can spend FP invoking aspects

### Compels
The GM may compel players, if compel is accepted by player add 1FP to the player's FP balance

### Invokes
Players may invoke aspects(their own or others) by spending FP. Take 1FP from player's balances; return an error if player has insufficient FP.

## Stress 
Track stress for each character/game entity. 
Stress boxes: 1st box absorbs 1 stress, 2nd box absorbs 2 stress, etc. 
### Consequences 
Consequences are invokable **Aspects**, absorbs 2, 4 and 6 stress.
Mild(2) is removed at the end of **Scenes**, Moderate and Severe need to be treated.

## Refresh command
Starts a new session, restoring everyone's fate points, and resets situational aspects

# Additional

## Clean up
Can choose to clean up after a period of time has elapsed.
Games can be persistent, i.e between sessions, and load/store from a public google sheet?


# References

## Avrae https://avrae.io/
A Dnd Bot, has essentially all the functionality required, just not the specifics.

## https://www.youtube.com/watch?v=_0LXIvLDhBM
Tutorial

## http://discordpy.readthedocs.io/en/latest/api.html
The API reference for python


# Installation

Need to install dependency for discord 

```
pip install discord 
```

# Running
the python code must be running, in order for it to occur.
