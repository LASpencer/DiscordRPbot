import unittest
from Consequence import Consequence

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.c = Consequence(2)

    def test_init(self):
        self.assertEqual("2 \naspects: \ntext: ",str(self.c), "did not init correctly")


if __name__ == '__main__':
    unittest.main()
