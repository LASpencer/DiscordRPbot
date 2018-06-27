"""

Author : Robin Phoeng
Date : 24/06/2018
"""

from Character import Character


class Game:
    """
    The game, containing all information of a game.
    """

    def __init__(self):
        self.characters = {}

    def new_character(self,name,player):
        """
        add a new character, tied to a player
        will delete old characters
        :param name: name of character
        :param player: player id
        """
        self.characters[player] = Character(name)

    def __str__(self):
        output = ""
        for cha in self.characters:
            output += str(cha) + "\n"
        return output

    def get_character(self,id):
        try:
            return self.characters[id]
        except KeyError:
            return None
