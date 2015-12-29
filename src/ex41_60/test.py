import unittest
from . import ex41, ex42, ex43, ex44, ex45, ex46, ex47, ex48,ex49, ex50, ex51, ex52, ex53

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
    def testEx46(self):
        self.assertEqual(ex46.golbach_other(),5777)
    def testEx47(self):
        self.assertEqual(ex47.find_consecutive(4),134043)
    def testEx48(self):
        self.assertEqual(ex48.self_powers(1000),"9110846700")
    def testEx49(self):
        self.assertEqual(ex49.prime_permutations(), "296962999629")
    def testEx50(self):
        self.assertEqual(ex50.consecutive_prime_sum(1000000), 997651)
    def testEx51(self):
        self.assertEqual(ex51.prime_digit_replacements(8), 121313)
    def testEx52(self):
        self.assertEqual(ex52.permuted_multiples(6), 142857)
    def testEx53(self):
        self.assertEqual(ex53.count_cnr_bigger(100,10**6), 4075)            
        
