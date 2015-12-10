import unittest
from . import ex22, ex24, ex25, ex26, ex27

class TestEx21_40(unittest.TestCase):
    def testEx22(self):
        self.assertEqual(ex22.name_scores(),871198282)
    
    def testEx24(self):
        self.assertEqual(ex24.lexographic_permutation(10,10**6),'2783915460')
    
    def testEx25(self):
        self.assertEqual(ex25.fibonacci_order_of_magnitude(1000),4782.0)
    
    def testEx26(self):
        self.assertEqual(ex26.max_reciprocal_cycle_length(),982)
        
    def testEx27(self):
        self.assertEqual(ex27.max_prime_sequence(),-59231)
            