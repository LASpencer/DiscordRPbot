import unittest
from Character import Character
from Aspect import Aspect

class CharacterAspectTest(unittest.TestCase):
    def setUp(self):
        self.c = Character()

    def test_add(self):
        self.assertTrue(self.c.add_aspect("On Fire"), " Did not return correct on successful add")
        self.assertEqual("on fire",self.c.display_aspect(),"Did not add aspect properly")
        self.assertFalse(self.c.add_aspect("On Fire"), "Did not return false on duplicate")
        self.assertEqual("on fire", self.c.display_aspect(), "Did not deny duplicate properly")

    def test_remove(self):
        self.assertTrue(self.c.add_aspect("On Fire"), " Did not return correct on successful add")
        self.assertEqual("on fire", self.c.display_aspect(), "Did not add aspect properly")
        self.assertTrue(self.c.remove_aspect("On Fire"), " Did not return true on successful removal")
        self.assertEqual("", self.c.display_aspect(), "Did not remove aspect properly")

    def test_remove_non_case_sensitive(self):
        self.assertTrue(self.c.add_aspect("On Fire"), " Did not return correct on successful add")
        self.assertEqual("on fire", self.c.display_aspect(), "Did not add aspect properly")
        self.assertTrue(self.c.remove_aspect("on FiRe"), " Did not return true on successful removal")
        self.assertEqual("", self.c.display_aspect(), "Did not remove aspect properly")

    def test_remove_does_not_exist(self):
        self.assertFalse(self.c.remove_aspect("on FiRe"), " Did not return false on no removal")

    def test_multiple_aspects(self):
        aspects = ["on fire", "dying", "bleeding", "chronic fatigue", "glowing"]

        for aspect in aspects:
            self.assertTrue(self.c.add_aspect(aspect), "Did not return correct on successful add")
            self.assertTrue(aspect in self.c.display_aspect(), "Did not add aspects into list")


if __name__ == '__main__':
    unittest.main()
