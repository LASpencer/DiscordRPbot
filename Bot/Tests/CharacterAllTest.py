import unittest
from Character import Character
from Bar import *

class CharacterAllTest(unittest.TestCase):

    def setUp(self):
        self.c = Character("jane")

    def test_init(self):
        self.assertEqual("jane\nAspects: \nSkills: ",str(self.c),"Did not properly initialise")

    def test_added(self):
        self.c.add_aspect("hiding")
        self.c.add_skill(1,"stealth")
        b = Bar("stress")
        b.add_box(Box(1))
        b.add_box(Box(2))
        b.add_box(Box(3))
        b.add_box(Box(4))
        self.c.add_bar(b)
        self.assertEqual("jane\n"
                         "Aspects: hiding\n"
                         "Skills: | 1 stealth |\n"
                         "stress [1] [2] [3] [4]",
                         str(self.c), "Did not format correctly")

    def test_example_2(self):
        self.c.add_aspect("hiding")
        self.c.add_aspect("taken")
        self.c.add_skill(1, "stealth")
        self.c.add_skill(1, "heal")
        b = Bar("stress")
        b.add_box(Box(1))
        b.add_box(Box(2))
        b.add_box(Box(3))
        b.add_box(Box(4))
        self.c.add_bar(b)
        self.assertEqual("jane\n"
                         "Aspects: hiding, taken\n"
                         "Skills: | 1 stealth | 1 heal |\n"
                         "stress [1] [2] [3] [4]",
                         str(self.c), "Did not format correctly")

if __name__ == '__main__':
    unittest.main()
