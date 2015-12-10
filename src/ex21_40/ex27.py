import primes
import itertools
import math
import time

def prime_sequence(b,c):
    for n in itertools.count():
        res = n**2 + b*n + c
        if not primes.is_prime(res):
            return (b,c,n) 
    
def max_prime_sequence():
    max_seq = (1,0)
    for c in primes.prime_generator():
        if c>1000:
            break
        for b in range(-c +1,1000): # when n = 1 then we have n -b +c so the result has to be at least 2
            res = prime_sequence(b,c)
            if res[2] > max_seq[0]:
                max_seq = (res[2], res[0] * res[1])
    return max_seq[1]
              
if __name__ == "__main__":
    start = time.clock()
    print(max_prime_sequence())
    end = time.clock()
    print("It took ",end - start," seconds")              
        