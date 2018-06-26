import unittest
from Aspect import *

# Not testing aspect, as it is a pure data class

class AspectContainerTest(unittest.TestCase):

    def setUp(self):
        self.container = AspectContainer()

    def test_add_get(self):
        self.assertTrue(self.container.add("On Fire"),"successful add not true")
        self.assertEqual("on fire",str(self.container),"Aspect not properly added")

    def test_add_duplicate(self):
        self.assertTrue(self.container.add("On Fire"),"successful add not true")
        self.assertFalse(self.container.add("On Fire"), "duplicate add false")
        self.assertEqual("on fire", str(self.container), "Aspect not properly added")

    def test_add_duplicate_non_case_sensitive(self):
        self.assertTrue(self.container.add("On Fire"),"successful add not true")
        self.assertFalse(self.container.add("on fire"), "duplicate add false")
        self.assertEqual("on fire", str(self.container), "Aspect not properly added")

    def test_remove(self):
        self.container.add("On Fire")
        self.assertTrue(self.container.remove("On Fire") is not None, "Did not return successful removal")
        self.assertEqual("", str(self.container), "Aspect not properly removed")

    def test_remove_non_case_sensitive(self):
        self.container.add("On Fire")
        self.container.remove("on fire")
        self.assertEqual("", str(self.container), "Aspect not properly removed")

    def test_multiple_aspects(self):
        aspects = ["on fire", "dying", "bleeding", "chronic fatigue", "glowing"]

        comma = 0
        for aspect in aspects:
            self.assertTrue(self.container.add(aspect), "Did not return correct on successful add")
            self.assertTrue(aspect in str(self.container), "Did not add aspects into list")
            self.assertEqual(comma, str(self.container).count(','), "Did not add commas correctly")
            comma += 1

if __name__ == '__main__':
    unittest.main()
