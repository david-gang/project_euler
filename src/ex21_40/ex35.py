from sympy import sieve
import collections
import time

def circular_primes(max_n):
    primes = list(sieve.primerange(2,max_n))
    count = 0
    prime_set = set(primes)
    for n in primes:
        isCircPrime = True
        n_queue = collections.deque(str(n))
        
        for _ in range(len(n_queue)):
            n_queue.rotate(1)
            if n_queue[0] == '0':
                continue           
            p_val = int("".join(n_queue))
            if p_val not in prime_set:
                isCircPrime = False
                break
        if isCircPrime:
             count = count +1
    return count

if __name__ == "__main__":     
    start = time.clock()   
    print(circular_primes(1000000))
    end = time.clock()
    print("It took ",end - start," seconds")
                
            
    