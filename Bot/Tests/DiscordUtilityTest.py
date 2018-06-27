import unittest
from DiscordUtility import *


"""
Check validity of utility functions used

"""

class DiscordUtilityTest(unittest.TestCase):
    def test_mention_valid(self):
        self.assertEqual("133546464495403008", valid_id("<@133546464495403008>"), "Did not accept valid value")
    def test_mention_invalid(self):
        self.assertEqual(None, valid_id("<@13354646449adsf403008>"), "Did not reject non-numeric")
    def test_mention_not(self):
        self.assertEqual(None, valid_id("<133546464495403008"), "Did not reject non-mention")
    def test_mention_none(self):
        self.assertEqual(None,valid_id(None),"Did not reject None")

    def test_role_valid(self):
        self.assertEqual("133546464495403008",valid_role("<@&133546464495403008>"),"Did not accept valid value")
    def test_role_invalid(self):
        self.assertEqual(None,valid_role("<@&13354646449adsf403008>"),"Did not reject non-numeric")
    def test_role_not(self):
        self.assertEqual(None,valid_role("<133546464495403008"),"Did not reject non-mention")
    def test_role_none(self):
        self.assertEqual(None,valid_role(None),"Did not reject None")
if __name__ == '__main__':
    unittest.main()
