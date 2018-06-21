"""

Author : Robin Phoeng
Date : 21/06/2018


"""
from Bar import *
from Aspect import *

"""
Represents a Character in the Fate SRD
"""


class Character:
    def __init__(self):
        self.bars = {}  # address bars by name
        self.aspects = AspectContainer()

    def get_bar(self, name):
        return self.bars[name]

    def add_bar(self, bar):
        assert isinstance(bar,Bar), "not adding bar"
        self.bars[bar.name] = bar

    '''
    :param bar: a string related to the box
    :param box: a index of which bar to use up
    '''
    def spend_box(self, bar, box):
        self.bars[bar][box].spend()

    '''
    :param bar: a string related to the box
    :param box: a index of which bar to use up
    '''
    def refresh_box(self, bar, box):
        self.bars[bar][box].refresh()

    def add_aspect(self,text):
        return self.aspects.add(Aspect(text))

    '''
    if aspect is present, return true
    if false, return false
    '''
    def remove_aspect(self,text):
        if self.aspects.remove(Aspect(text)) is None:
            return False
        else:
            return True

