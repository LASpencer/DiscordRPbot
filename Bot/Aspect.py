"""

Author : Robin Phoeng
Date : 21/06/2018
"""


"""
A container for aspects
this is separated in the event that a different storing scheme is desired.
"""
class AspectContainer:

    def __init__(self):
        self.aspects = []

    def __str__(self):
        output = ""
        for aspect in self.aspects:
            output += str(aspect) + " "
        output = output[0:len(output)-1] # remove the last space
        return output

    '''
    Does not allow repeats
    '''
    def add(self,aspect):
        assert isinstance(aspect,Aspect), "Only store aspects"

        for a in self.aspects:
            if a.text.lower() == aspect.text.lower():
                return False

        # successfully added
        self.aspects.append(aspect)
        return True

    def __getitem__(self, index):
        assert isinstance(index,int), "must be integer for iterable"
        return self.aspects[index]

    '''
    Return removed item, or None if it doesn't exist
    '''
    def remove(self,text):
        # we care not for letter case
        for aspect in self.aspects:
            if aspect.text.lower() == text.lower():
                self.aspects.remove(aspect)
                return aspect
        return None

"""
A descriptor of a character
An aspect can have the same text as another aspect.
"""
class Aspect:

    def __init__(self,text):
        self.text = text

    def __str__(self):
        return self.text

