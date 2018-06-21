import unittest
from Character import *
from Bar import *
class CharacterBarTest(unittest.TestCase):
    def setUp(self):
        self.c = Character()
        self.bar = Bar("Test")
        self.bar.add_box(Box(1))
        self.bar.add_box(Box(2))
        self.bar.add_box(Box(3))
        self.bar.add_box(Box(4))
        self.c.add_bar(self.bar)

    def test_add(self):
        self.assertEqual(self.bar,self.c.get_bar("Test"),"Did not properly add bar to character")

    def test_spend(self):
        self.c.spend_box("Test",1)
        self.assertTrue(self.bar[1].used,"Did not spend the correct box")
        self.assertFalse(self.bar[2].used, "Did not spend the correct box")
        self.assertFalse(self.bar[3].used, "Did not spend the correct box")
        self.assertFalse(self.bar[4].used, "Did not spend the correct box")
        self.c.spend_box("Test", 2)
        self.assertTrue(self.bar[1].used, "Did not spend the correct box")
        self.assertTrue(self.bar[2].used, "Did not spend the correct box")
        self.assertFalse(self.bar[3].used, "Did not spend the correct box")
        self.assertFalse(self.bar[4].used, "Did not spend the correct box")

    def test_refresh(self):
        # spend all
        self.bar[1].spend()
        self.bar[2].spend()
        self.bar[3].spend()
        self.bar[4].spend()
        self.c.refresh_box("Test", 1)

        self.assertFalse(self.bar[1].used, "Did not refresh the correct box")
        self.assertTrue(self.bar[2].used, "Did not refresh the correct box")
        self.assertTrue(self.bar[3].used, "Did not refresh the correct box")
        self.assertTrue(self.bar[4].used, "Did not refresh the correct box")

        self.c.refresh_box("Test", 3)
        self.assertFalse(self.bar[1].used, "Did not refresh the correct box")
        self.assertTrue(self.bar[2].used, "Did not refresh the correct box")
        self.assertFalse(self.bar[3].used, "Did not refresh the correct box")
        self.assertTrue(self.bar[4].used, "Did not refresh the correct box")


if __name__ == '__main__':
    unittest.main()
