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
        self.assertEqual("bar [2]",str(self.b), "Added box not properly appended to display")
        self.assertEqual(self.b[1],box,"Box not properly added")
        self.b.remove_box(0)
        self.assertEqual("bar", str(self.b), "Box not removed")

    def test_bar_spend_refresh(self):
        box1 = Box(1)
        box2 = Box(2)
        self.b.add_box(box1)
        self.b.add_box(box2)
        box1.spend()

        self.b.spend()
        for box in self.b:
            self.assertTrue(box.used,"Not all boxes spent")

        self.b.refresh()
        for box in self.b:
            self.assertFalse(box.used,"Not all boxes refreshed")


if __name__ == '__main__':
    unittest.main()
