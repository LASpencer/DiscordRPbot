import unittest

import BarFactory

class BarFactoryTest(unittest.TestCase):
    def test_bar_default(self):
        b = BarFactory.bar_default("stress")
        self.assertEqual("stress [1] [2]",str(b),"Did not create a bar properly")

    def test_bar_consequence(self):
        b = BarFactory.bar_consequence("stress")
        self.assertEqual("consequences [2] [4] [6]",str(b),"Did not create a bar properly")


if __name__ == '__main__':
    unittest.main()
