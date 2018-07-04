import unittest

from Character import *
import CharacterSave

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.c = Character("test")

    def test_save(self):
        CharacterSave.save(self.c)
        # check that a file called test.txt is created
        """
        test 0
        con_bar consequence
        """

        cha = CharacterSave.load("test")

        self.assertEqual(str(self.c),str(cha),"did not save/load properly")

    def test_save_aspect(self):
        self.c.add_aspect("hello")
        CharacterSave.save(self.c)
        # check that a file called test.txt is created with
        """
        test 0
        aspect hello
        con_bar consequence
        """
        cha = CharacterSave.load("test")

        self.assertEqual(str(self.c), str(cha), "did not save/load properly")

    def test_save_aspect_multiple(self):
        self.c.add_aspect("hello")
        self.c.add_aspect("field")
        self.c.add_aspect("able")
        CharacterSave.save(self.c)
        # check that a file called test.txt is created with
        """
        test 0
        aspect hello
        aspect field
        aspect able
        con_bar consequence
        """
        cha = CharacterSave.load("test")

        self.assertEqual(str(self.c), str(cha), "did not save/load properly")

    def test_save_bar(self):
        self.c.add_bar(Bar("physical"))
        CharacterSave.save(self.c)
        # check that a file called test.txt is created
        """
        test 0
        physical [1] [2] [3] [4]
        con_bar consequence
        """
        cha = CharacterSave.load("test")

        self.assertEqual(str(self.c), str(cha), "did not save/load properly")

    def test_save_boxes(self):
        b = Bar("physical")
        b.add_box(Box(1))
        b.add_box(Box(3))
        self.c.add_bar(b)

        CharacterSave.save(self.c)
        # check that a file called test.txt is created
        """
        test 0
        physical [1] [3]
        con_bar consequence
        """
        cha = CharacterSave.load("test")

        self.assertEqual(str(self.c), str(cha), "did not save/load properly")

    def test_save_boxes_used(self):
        b = Bar("physical")
        b.add_box(Box(1))
        b.add_box(Box(3))
        b[1].spend()
        self.c.add_bar(b)

        CharacterSave.save(self.c)
        # check that a file called test.txt is created
        """
        test 0
        physical ~~[1]~~ [3]
        con_bar consequence
        """
        cha = CharacterSave.load("test")

        self.assertEqual(str(self.c), str(cha), "did not save/load properly")

    def test_save_bars(self):
        b = Bar("physical")
        b2 = Bar("mental")
        b.add_box(Box(1))
        b.add_box(Box(3))
        b[1].spend()
        self.c.add_bar(b)
        self.c.add_bar(b2)

        CharacterSave.save(self.c)
        # check that a file called test.txt is created
        """
        test 0
        physical ~~[1]~~ [3]
        mental 
        con_bar consequence
        """
        cha = CharacterSave.load("test")

        self.assertEqual(str(self.c), str(cha), "did not save/load properly")

    def test_save_skill(self):
        self.c.add_skill(4,"stealth")
        CharacterSave.save(self.c)
        # check that a file called test.txt is created
        """
        test 0
        skill 4 stealth
        con_bar consequence
        """
        cha = CharacterSave.load("test")

        self.assertEqual(str(self.c), str(cha), "did not save/load properly")

    def test_save_skills(self):
        self.c.add_skill(4,"stealth")
        self.c.add_skill(3, "heal")
        self.c.add_skill(1, "stab")
        CharacterSave.save(self.c)
        # check that a file called test.txt is created
        """
        test 0
        skill 4 stealth
        skill 3 heal
        skill 1 stab
        con_bar consequence
        """
        cha = CharacterSave.load("test")

        self.assertEqual(str(self.c), str(cha), "did not save/load properly")

    def test_save_consequence(self):
        self.c.consequence_bar.add_box(Box(2))
        self.c.consequence_bar.add_box(Box(4))
        self.c.add_consequence(2)
        CharacterSave.save(self.c)
        """
        test 0
        con_bar consequence ~~[2]~~ [4]
        con 2
        aspects:
        text:
        """
        cha = CharacterSave.load("test")

        self.assertEqual(str(self.c), str(cha), "did not save/load properly")

    # TODO add a save all test


if __name__ == '__main__':
    unittest.main()
