import math
import time
from itertools import product
def digit_factorials():
    candidate_ranges = []
    n = 2
    fact_nine = math.factorial(9)
    while True:
        if n * fact_nine < 10**(n-1):
            break
        candidate_ranges.append(n)
        n = n+1
    fact_digits = [math.factorial(i) for i in range(0,10)]
    char_digits = [str(i) for i in range(0,10)]
    s = 0
    for n in candidate_ranges:
        gens = [range(1,10)]
        gens.extend(range(0,10) for _ in range(1,n))
        for perm in product(*gens):
            res = sum(fact_digits[p] for p in perm)
            char_res = "".join(char_digits[p] for p in perm)
            if char_res == str(res):
                s = s+res
                
    return s
                
        
        
        
    
            
        
if __name__ == "__main__":     
    start = time.clock()   
    print(digit_factorials())
    end = time.clock()
    print("It took ",end - start," seconds")