import unittest
from . import ex41, ex42, ex43, ex44, ex45

class TestEx41_60(unittest.TestCase):
    def testEx41(self):
        self.assertEqual(ex41.pandigital_prime(),7652413)
    def testEx42(self):
        self.assertEqual(ex42.triangle_numbers(),162)
    def testEx43(self):
        self.assertEqual(ex43.substring_divisibiliy_sum(),16695334890)
    def testEx44(self):
        self.assertEqual(ex44.check_pentagonal_number(),5482660)
    def testEx45(self):
        self.assertEqual(ex45.find_second_equality(),1533776805)
