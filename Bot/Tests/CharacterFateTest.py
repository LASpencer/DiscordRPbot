import unittest

from Character import Character

class CharacterFateTest(unittest.TestCase):
    def setUp(self):
        self.c = Character("bob",refresh_rate=3)

    def test_initialise(self):
        self.assertEqual(0,self.c.get_fate(),"Did not initialise at 0 fate")

    def test_change_positive(self):
        self.c.change_fate(10)
        self.assertEqual(10,self.c.get_fate(),"did not change fate by 10")

    def test_change_negative(self):
        self.c.change_fate(10)
        self.c.change_fate(-2)
        self.assertEqual(8, self.c.get_fate(), "did not change fate by 10 - 2")

    def test_refresh_less(self):
        self.c.refresh_fate()
        self.assertEqual(3,self.c.get_fate(), "did not refresh to 3")

    def test_refresh_more(self):
        self.c.change_fate(10)
        self.c.refresh_fate()
        self.assertEqual(10,self.c.get_fate(), "did not keep 10 fate")

if __name__ == '__main__':
    unittest.main()
