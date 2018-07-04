"""

Author : Robin Phoeng
Date : 1/07/2018
"""
from Character import Character
import BarFactory


def Player(name,refresh_rate=3):
    cha = Character(name,refresh_rate)
    cha.add_bar(BarFactory.bar_default("physical"))
    cha.add_bar(BarFactory.bar_default("mental"))
    cha.consequence_bar = BarFactory.bar_consequence("consequence")
    return cha

def Default(name):
    cha = Character(name)
    return cha
