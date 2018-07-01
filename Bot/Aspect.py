"""

Author : Robin Phoeng
Date : 22/06/2018
"""

class AspectContainer:
    """
    A container for aspects
    this is separated in the event that a different storing scheme is desired.
    """

    def __init__(self):
        self.aspects = []

    def __str__(self):
        output = ""
        for aspect in self.aspects:
            output += str(aspect) + ", "
        output = output[0:len(output)-2] # remove the last space and comma
        return output

    def add(self,text):
        """
        Adds an aspect to the container
        Assumes all aspect text is in lower case
        :param text: text of the new aspect
        :return: False if duplicate, true if added
        """

        text_lower = text.lower()
        for aspect in self.aspects:
            if aspect.text == text_lower:
                return False

        # successfully added
        self.aspects.append(Aspect(text_lower))
        return True

    def __getitem__(self, index):
        assert isinstance(index,int), "must be integer for iterable"
        return self.aspects[index]

    def remove(self,text):
        """
        remove an aspect
        assumes unique aspects and non-case sensitive
        :param text: the text of the aspect to remove
        :return: the aspect if present
        """
        # we care not for letter case
        text_lower = text.lower()
        for aspect in self.aspects:
            if aspect.text == text_lower:
                self.aspects.remove(aspect)
                return aspect
        return None


class Aspect:
    """
    A descriptor of a character
    An aspect can have the same text as another aspect.
    """
    def __init__(self,text):
        self.text = text

    def __str__(self):
        return self.text


