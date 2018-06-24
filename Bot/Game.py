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
        self.players = {}
        self.gm = None


    def set_gm(self,id):
        self.gm = id

    def add_player(self,player):
        #TODO check if player is added already
        self.players[player] = None

    def __str__(self):
        output = "GM :" + (self.gm if self.gm is not None else "N/A")
        output += "\n"
        for player in self.players:
            output += player + "\n"
        return output