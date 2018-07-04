"""

Author : Robin Phoeng
Date : 21/06/2018


"""
from Bar import *
from Aspect import *
from Skill import *
import BarFactory
from Consequence import *
"""
Represents a Character in the Fate SRD
"""

class Character:
    def __init__(self,name, refresh_rate=3):
        self.name = name
        self.bars = {}  # address bars by name
        self.aspects = AspectContainer()
        self.skills = SkillContainer()
        self.fate = 0
        self.refresh_rate = refresh_rate
        self.consequence_bar = Bar("consequence")
        self.consequences = []

    def get_fate(self):
        return self.fate

    def change_fate(self,change):
        """
        Change the fate points
        the fate points is always greater than 0
        :param change: the amount to change by
        :return: True if changed, false otherwise
        """
        temp = self.fate + change
        if temp < 0:
            return False
        self.fate = temp
        return True

    def refresh_fate(self):
        """
        Returns fate to a minimum, otherwise doesn't change
        """
        self.fate = self.fate if self.fate >= self.refresh_rate else self.refresh_rate

    def set_refresh_fate(self,rate):
        """
        Sets the refresh rate
        :param rate:
        """
        self.refresh_rate = rate

    def get_bar(self, name):
        '''
        Gets a bar
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


    def refresh_bar(self,text):
        """
        Delegate to bar.refresh
        :param text: name of bar
        """
        self.bars[text.lower()].refresh()

    def spend_bar(self,text):
        """
        Delegate to bar.spend
        :param text: name of bar
        """
        self.bars[text.lower()].spend()

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

    def add_skill(self,level,name):
        """
        Deletegate to skills
        :param level: the level of the skill
        :param name: the name of the skill
        :return: True if added
        """
        return self.skills.add(level,name)

    def get_skill_level(self,name):
        """
        Delegate to skills
        :param name: the name of the skill
        :return: the level of the skill, none otherwise
        """
        return self.skills.get_level(name)

    def remove_skill(self,name):
        """
        Delegate to skills
        :param name: the name of the skill
        :return: the skill that is removed, None otherwise
        """
        return self.skills.remove(name)

    def get_name(self):
        return self.name

    def __str__(self):
        output = ""
        output += self.name
        # add aspects
        output += "\nAspects: "
        output += str(self.aspects)
        # add skills
        output += "\nSkills: "
        output += str(self.skills)

        for bar in self.bars:
            output += "\n"
            output += str(self.bars[bar])

        output += "\n"
        output += str(self.consequence_bar)
        return output

    def add_consequence(self,modifier):
        """
        Adds a consequence on a modifier
        :param modifier: multiple of 2
        :return: True if added, false otherwise
        :raise ValueError: modifier not divisible by 2
        """
        # check that modifier is a multiple of 2
        if modifier % 2 != 0:
            raise ValueError("modifier not divisible by 2")

        index = modifier // 2
        # check bar is spent or not
        if self.consequence_bar[index-1].is_spent():
            return False

        self.consequences.append(Consequence(modifier))
        self.consequence_bar[index-1].spend()

    def remove_consequence(self,modifier):
        """
        remove a consequence on a modifier
        :param modifier: multiple of 2
        :return: True if removed, false otherwise
        :raise ValueError: modifier not divisible by 2
        """
        # check that modifier is a multiple of 2
        if modifier % 2 != 0:
            raise ValueError("modifier not divisible by 2")

        index = modifier //2
        # check bar is spent or not
        if self.consequence_bar[index-1].is_spent():
            return False

        for cons in self.consequences:
            if cons.get_modifier() == modifier:
                self.consequences.remove(cons)
                break
        self.consequence_bar[index-1].refresh()

    def get_consequence(self,modifier):
        """
        returns the consequence at a modifier
        :param modifier: modifier divisible by 2
        :return: consequence if found, None otherwise
        :raise ValueError: modifier not divisible by 2
        """
        if modifier % 2 != 0:
            raise ValueError("modifier not divisible by 2")

        index = modifier //2
        # check bar is spent or not
        if not self.consequence_bar[index-1].is_spent():
            return None # no consequence

        for cons in self.consequences:
            if cons.get_modifier() == modifier:
                return cons
