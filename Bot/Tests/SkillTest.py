import unittest
from Skill import *

class SkillTest(unittest.TestCase):

    def setUp(self):
        self.container = SkillContainer()

    def test_init(self):
        self.assertEqual("", str(self.container), "Did not initialise correctly")

    def test_add(self):
        self.assertTrue(self.container.add(4,"Stealth"),"did not return true on successful add")
        self.assertEqual("| 4 stealth |", str(self.container), "Did not properly add skill")

    def test_add_duplicate(self):
        self.container.add(4, "stealth")
        self.assertFalse(self.container.add(2, "stealth"),"Did not return false on duplicate")
        self.assertEqual(4,self.container.get_level("stealth"),"duplicate overwrote level")

    def test_get(self):
        self.container.add(4, "stealth")
        self.assertEqual(4,self.container.get_level("stealth"), "did not get proper level")

    def test_get_non_case_sensitive(self):
        self.container.add(4, "stealth")
        self.assertEqual(4,self.container.get_level("Stealth"), "did not get proper level")

    def test_get_empty(self):
        self.assertEqual(None,self.container.get_level("Stealth"), "did not return None on no skill")

    def test_remove(self):
        self.assertTrue(self.container.add(4, "Stealth"), "did not return true on successful add")
        self.assertEqual("| 4 stealth |", str(self.container), "Did not properly add skill")
        self.assertNotEqual(None,self.container.remove("Stealth"), "returned None on successful removal")
        self.assertEqual("", str(self.container), "Did not properly remove skill")

    def test_remove_non_case_sensitive(self):
        self.assertTrue(self.container.add(4, "Stealth"), "did not return true on successful add")
        self.assertEqual("| 4 stealth |", str(self.container), "Did not properly add skill")
        self.assertNotEqual(None, self.container.remove("STEALTH"), "returned None on successful removal")
        self.assertEqual("", str(self.container), "Did not properly remove skill")

    def test_remove_does_not_exist(self):
        self.assertEqual(None, self.container.remove("STEALTH"), "returned None on successful removal")
        self.assertEqual("", str(self.container), "Did not properly remove skill")

    def test_sorted_display(self):
        skills = [(1,"strike"),(1,"heal"),(2,"create"),(3,"hi"),(4,"tell"),(1,"well"), (4,"steal")]

        for skill in skills:
            self.container.add(skill[0],skill[1])

        self.assertEqual("| 4 tell | 4 steal | 3 hi | 2 create | 1 strike | 1 heal | 1 well |",str(self.container), "not proper displayed")

if __name__ == '__main__':
    unittest.main()
