"""

Author : Robin Phoeng
Date : 28/06/2018
"""

from Aspect import *

class Consequence:
    """
    This will need to handle a consequence type
    """
    def __init__(self,modifier,name= None):
        self.name = "" if name is None else name
        self.modifier = modifier
        self.aspects = AspectContainer()
        self.text = ""

    def get_modifier(self):
        return self.modifier

    def add_aspect(self,text):
        self.aspects.add(text)

    def remove_aspect(self,text):
        self.aspects.remove(text)

    def set_text(self,text):
        self.text = text

    def __str__(self):
        output = "%d %s\n" % (self.modifier,self.name)
        output += "aspects: %s" % str(self.aspects)
        output += "\ntext: %s" % self.text
        return output