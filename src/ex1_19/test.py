import unittest
from . import ex19

class TestEx1_19(unittest.TestCase):
    def testEx19(self):
        self.assertEqual(ex19.count_sundays_first_of_month(),171)