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
    def __init__(self, refresh_rate = 3):
        self.bars = {}  # address bars by name
        self.aspects = AspectContainer()
        self.fate = 0
        self.refresh_rate = refresh_rate

    def get_fate(self):
        return self.fate

    def change_fate(self,change):
        """
        Change the fate points
        TODO negotiate maximum, minimum
        :param change: the amount to change by
        """
        self.fate += change

    def refresh_fate(self):
        """
        Returns fate to a minimum, otherwise doesn't change
        """
        self.fate = self.fate if self.fate >= self.refresh_rate else self.refresh_rate

    def get_bar(self, name):
        '''
        Gets a bar,
        :param name: name of bar, non-case-sensitive
        :return: Bar, or None if it does not exist
        '''
        try:
            return self.bars[name.lower()]
        except KeyError:
            return None

    def add_bar(self, bar):
        '''
        Adds a bar, with a non-case-sensitive name
        :param bar: the bar to add
        '''
        assert isinstance(bar,Bar), "not adding bar"
        self.bars[bar.name.lower()] = bar

    def remove_bar(self,text):
        """
        Remove a bar from a character
        It requires that we are removing a bar object
        This is non-case-sensitive
        :param text: the name of bar to remove
        :return: the Bar removed, None otherwise
        """
        return self.bars.pop(text.lower(), None)

    def spend_box(self, bar, box):
        """
        spend a box of a bar
        This currently depends on how the bar is implemented
        (bar currently assumed implemented as array)
        :param bar: the name of the bar non-case-sensitive
        :param box: the index of the box
        """
        self.bars[bar.lower()][box].spend()

    def refresh_box(self, bar, box):
        """
        refresh a box of a bar so it can be used again
        This currently depends on how the bar is implemented
        (bar currently assumed implemented as array)
        :param bar: the name of the bar non-case-sensitive
        :param box: the index of the box
        """
        self.bars[bar.lower()][box].refresh()

    def add_aspect(self,text):
        """
        Delegate function
        Adds an aspect to the character
        this is non-case sensitive
        :param text: the aspect to add
        :return: true if added, false if not
        """
        return self.aspects.add(text)

    def remove_aspect(self,text):
        """
        Remove an aspect
        This is non-case sensitive
        :param text: the aspect to remove
        :return: True if removed, false if not removed (either not present or unsuccessful)
        """
        return self.aspects.remove(text) is not None

    def display_aspect(self):
        return str(self.aspects)


