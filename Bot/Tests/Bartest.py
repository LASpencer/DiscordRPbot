import unittest
from Bar import Bar
from Bar import Box

class BarTest(unittest.TestCase):

    def setUp(self):
        self.b = Bar("bar")

    def test_Bar_Init(self):
        self.assertEqual("bar",str(self.b),"empty bar string not displaying correctly")

    def test_Bar_box(self):
        box = Box(2)
        self.b.add_box(box)
        self.assertEqual("bar\nSize: 2 Used :N",str(self.b), "Added box not properly appended to display")
        self.assertEqual(self.b[0],box,"Box not properly added")


if __name__ == '__main__':
    unittest.main()
