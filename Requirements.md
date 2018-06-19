# Basics

## Dice roll
Fudge dice roller, 3-sided dice (-1,0,1)
Rolls 4 times and returns sum.

- Can use a discrete distribution, and one random function call to improve speed

## Aspects
Aspects are tied to characters, can be **invoked** and **compelled**

## Fate Points
Fate points are the currency for game influence. Needs to be tracked. 
- Refresh: when new session starts, if the player's FP < Refresh, set FP to Refresh
- Players gains FP for accepting compels, and can spend FP invoking aspects

## Compels
The GM may compel players, if compel is accepted by player add 1FP to the player's FP balance

## Invokes
Players may invoke aspects(their own or others) by spending FP. Take 1FP from player's balances; return an error if player has insufficient FP.

## Refresh command
Starts a new session, restoring everyone's fate points, and situational aspects

# Additional

## Clean up
Can choose to clean up after a period of time has elapsed.
Games can be persistent, i.e between sessions, and load/store from a public google sheet?


# References

## Avrae https://avrae.io/
A Dnd Bot, has essentially all the functionality required, just not the specifics.

## https://www.youtube.com/watch?v=_0LXIvLDhBM
Tutorial

# Installation

Need to install dependency for discord 

```
pip install discord 
```

# Running
the python code must be running, in order for it to occur.
