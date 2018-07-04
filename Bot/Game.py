"""

Author : Robin Phoeng
Date : 24/06/2018
"""

from Character import Character
import CharacterFactory

class Game:
    """
    The game, containing all information of a game.
    """

    def __init__(self):
        self.characters = {}
        self.players = {}

    def new_character(self,name):
        """
        add a new character
        will delete old characters of the same name
        :param name: name of character
        """
        n = name.lower()
        self.characters[n] = CharacterFactory.Default(n)

    def remove_character(self,name):
        """
        removes a character, returning it if found
        :param name: name to remove
        :return: character if found, None otherwise
        """
        try:
            return self.characters.pop(name.lower())
        except KeyError:
            return None

    def player_link_character(self, name, player):
        """
        links a player to a character, if no character exists it will
        create one
        :param name: name of character
        :param player: True if linked, False if new character
        """
        n = name.lower()
        linked = True
        if n not in self.characters.keys():
            self.characters[n] = CharacterFactory.Player(n)
            linked = False
        self.players[player] = n
        return linked

    def __str__(self):
        output = ""
        for cha in self.characters:
            output += str(cha) + "\n"
        return output

    def get_character(self,name):
        """
        gets a character
        :param name: either a id, or the name of the character
        :return: None if character doesnt exist, character otherwise
        """
        # check numeric
        if name.isdigit():
            n = self.players[name]
        else:
            n = name.lower()

        try:
            return self.characters[n]
        except KeyError:
            return None

    def refresh(self):
        """
        Refresh game state.
        """
        for cha in self.players.items():
            assert isinstance(cha,Character)
            cha.refresh_fate()