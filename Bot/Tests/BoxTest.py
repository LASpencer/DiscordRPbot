import unittest
from Bar import Box

class BoxTest(unittest.TestCase):
    def setUp(self):
        self.b = Box(2)
    def test_box_init(self):
        self.assertFalse(self.b.used,"not set to un-used")
        self.assertEqual("[2]", str(self.b), "Box init not displayed correctly")

    def test_box_spent(self):
        self.b.spend()
        self.assertTrue(self.b.used, "not set to used")
        self.assertEqual("~~[2]~~", str(self.b), "Box spent not displayed correctly")
        self.b.refresh()
        self.assertFalse(self.b.used, "not set to un-used")
        self.assertEqual("[2]", str(self.b), "Box refresh not displayed correctly")


if __name__ == '__main__':
    unittest.main()
