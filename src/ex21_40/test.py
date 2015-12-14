import unittest
from . import ex22, ex24, ex25, ex26, ex27, ex28, ex29, ex30, ex31, ex32, ex33

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
        
    def testEx28(self):
        self.assertEqual(ex28.spiral_diagonals_sum(1001),669171001)
        
    def testEx29(self):
        self.assertEqual(ex29.distinct_powers(100, 100),9183)
        
    def testEx30(self):
        self.assertEqual(ex30.digit_powers(5),443839)
        
    def testEx31(self):
        self.assertEqual(ex31.coin_sums(200),73682)
    
    def testEx32(self):
        self.assertEqual(ex32.pandigital_products(), 45228)
        
    def testEx33(self):
        self.assertEqual(ex33.cancel_digit_fractions(), 100)
            