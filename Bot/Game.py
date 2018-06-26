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
        self.players = []
        self.characters = {}
        self.gm = None


    def set_gm(self,id):
        self.gm = id

    def add_player(self,player):
        """
        Add a player if not already in game
        :param player: the id of the player
        :return: True if added, False if not
        """
        if player not in self.players:
            self.players.append(player)
            return True
        return False

    def new_character(self,name,player):
        """
        add a new character, tied to a player
        will delete old characters
        :param name: name of character
        :param player: player id
        """
        self.characters[player] = Character(name)

    def remove_player(self,id):
        """
        Remove a player
        :param id: the id of player to remove
        :return: True if removed, False if not
        """
        for p in self.players:
            if p == id:
                return self.players.remove(p)

        return False

    def __str__(self):
        output = "GM :" + (self.gm if self.gm is not None else "N/A")
        output += "\n"
        for player in self.players:
            output += player + "\n"
        return output

    def player_in_game(self,id):
        """
        query method for player
        :param id: id of player
        :return:
        """
        return id in self.players

    def get_character(self,id):
        try:
            return self.characters[id]
        except KeyError:
            return None
