import unittest

from BarFactory import BarFactory

class BarFactoryTest(unittest.TestCase):
    def test_bar_default(self):
        b = BarFactory.bar_default("stress")
        self.assertEqual("stress \033[0;32m[1]\033[0m \033[0;32m[2]\033[0m \033[0;32m[3]\033[0m \033[0;32m[4]\033[0m",str(b),"Did not create a bar properly")

    def test_bar_consequence(self):
        b = BarFactory.bar_consequence("stress")
        self.assertEqual("stress \033[0;32m[2]\033[0m \033[0;32m[4]\033[0m \033[0;32m[6]\033[0m",str(b),"Did not create a bar properly")


if __name__ == '__main__':
    unittest.main()
