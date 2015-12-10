import itertools
import math
from bisect import bisect_left
import time

primes = [2,3]
highest_number_checked_for_primes = 3
def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def is_prime(n):
    global highest_number_checked_for_primes
    if n<2:
        return False
    if n<=highest_number_checked_for_primes:
        return binary_search(primes, n) != -1
    
    n_root = int(math.sqrt(n))
    
    if n_root > highest_number_checked_for_primes:
        for i in range(highest_number_checked_for_primes +1, n_root +1):
            if is_prime(i):
                primes.append(i)
        highest_number_checked_for_primes = n_root
        
    for p in primes:
        if p > n_root:
            break
        if n %p ==0:
            return False
    return True
                
        
            
            
    
        
    
    
def prime_generator():
    yield 2;
    yield 3;
    for i in itertools.count():
        n1 = 6*i-1
        n2 = 6*i+1
        if is_prime(n1):
            yield n1
        if is_prime(n2):
            yield n2

if __name__ == "__main__":	
	count =0
	for i in prime_generator():
		if i>100000000:
			break
		count = count + 1
		if count %100000 == 0:
			print(time.strftime("%H:%M:%S", time.gmtime()),"count", count, "prime", i)
	print(primes)