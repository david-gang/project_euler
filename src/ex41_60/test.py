import unittest
from . import ex41

class TestEx41_60(unittest.TestCase):
    def testEx41(self):
        self.assertEqual(ex41.pandigital_prime(),7652413)
