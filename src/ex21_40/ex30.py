from sympy import factorint
import time
from itertools import product
def digit_powers(m):
    candidate_ranges = []
    n = 1
    while True:
        if n * (9**m)< 10**(n-1):
            break
        if 2 **m <  2* (10**n):
            candidate_ranges.append(n)
        n = n+1
    
    power_digits = [i**m for i in range(0,10)]
    char_digits = [str(i) for i in range(0,10)]
    s = 0
    for n in candidate_ranges:
        if n==1:
            gens = [range(2,10)]
        else:
            gens = [range(1,10)]
            gens.extend(range(0,10) for _ in range(1,n))
        for perm in product(*gens):
            res = sum(power_digits[p] for p in perm)
            char_res = "".join(char_digits[p] for p in perm)
            if char_res == str(res):
                s = s+res
                
    return s
                
        
        
        
    
            
        
if __name__ == "__main__":     
    start = time.clock()   
    print(digit_powers(5))
    end = time.clock()
    print("It took ",end - start," seconds")