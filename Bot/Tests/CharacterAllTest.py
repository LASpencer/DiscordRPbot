import unittest
from Character import Character
from Bar import *

class CharacterAllTest(unittest.TestCase):

    def setUp(self):
        self.c = Character("jane")

    def test_init(self):
        self.assertEqual("jane\n"
                         "Aspects: \n"
                         "Skills: \n"
                         "physical [1] [2]\n"
                         "mental [1] [2]\n"
                         "consequence [2] [4] [6]",str(self.c),"Did not properly initialise")

    def test_added(self):
        self.c.add_aspect("hiding")
        self.c.add_skill(1,"stealth")
        self.assertEqual("jane\n"
                         "Aspects: hiding\n"
                         "Skills: | 1 stealth |\n"
                         "physical [1] [2]\n"
                         "mental [1] [2]\n"
                         "consequence [2] [4] [6]",
                         str(self.c), "Did not format correctly")

    def test_example_2(self):
        self.c.add_aspect("hiding")
        self.c.add_aspect("taken")
        self.c.add_skill(1, "stealth")
        self.c.add_skill(1, "heal")
        self.assertEqual("jane\n"
                         "Aspects: hiding, taken\n"
                         "Skills: | 1 stealth | 1 heal |\n"
                         "physical [1] [2]\n"
                         "mental [1] [2]\n"
                         "consequence [2] [4] [6]",
                         str(self.c), "Did not format correctly")

if __name__ == '__main__':
    unittest.main()
