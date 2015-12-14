import time
from sympy import isprime
from itertools import permutations
def pandigital_prime():
    max_p = 0
    for n in range(1,10):
        all_digits = [str(i) for i in range(1,n+1)]
        for perm in permutations(all_digits):
            p = int("".join(perm))
            if isprime(p):
                max_p = max(p, max_p)
    return max_p

if __name__ == "__main__":     
    start = time.clock()   
    print(pandigital_prime())
    end = time.clock()
    print("It took ",end - start," seconds")             
        

                
        
        
        
    