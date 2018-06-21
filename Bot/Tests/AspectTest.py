import unittest
from Aspect import *

# Not testing aspect, as it is a pure data class

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.container = AspectContainer()

    def test_add_get(self):
        aspect = Aspect("On Fire")
        self.assertTrue(self.container.add(aspect),"successful add not true")
        self.assertEqual("On Fire",str(self.container),"Aspect not properly added")
        self.assertEqual(aspect,self.container[0],"Aspect not added in correct position")

    def test_add_duplicate(self):
        aspect = Aspect("On Fire")
        aspect2 = Aspect("On Fire")
        self.assertTrue(self.container.add(aspect),"successful add not true")
        self.assertFalse(self.container.add(aspect2), "duplicate add false")
        self.assertEqual("On Fire", str(self.container), "Aspect not properly added")
        self.assertEqual(aspect, self.container[0], "Aspect not added in correct position")

    def test_add_duplicate_non_case_sensitive(self):
        aspect = Aspect("On Fire")
        aspect2 = Aspect("on Fire")
        self.assertTrue(self.container.add(aspect),"successful add not true")
        self.assertFalse(self.container.add(aspect2), "duplicate add false")
        self.assertEqual("On Fire", str(self.container), "Aspect not properly added")
        self.assertEqual(aspect, self.container[0], "Aspect not added in correct position")

    def test_remove(self):
        aspect = Aspect("On Fire")
        self.container.add(aspect)
        self.assertEqual(aspect, self.container[0], "Aspect not added in correct position")
        self.container.remove("On Fire")
        self.assertEqual("", str(self.container), "Aspect not properly removed")

    def test_remove_non_case_sensitive(self):
        aspect = Aspect("On Fire")
        self.container.add(aspect)
        self.assertEqual(aspect, self.container[0], "Aspect not added in correct position")
        self.container.remove("on fire")
        self.assertEqual("", str(self.container), "Aspect not properly removed")


    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
