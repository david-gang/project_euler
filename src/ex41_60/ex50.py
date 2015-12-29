import time
from sympy import primerange

def get_largest_consecutive(primes, prime_set,i):
    largest_prime = (-1,0)
    s = 0
    prime_len = len(primes)
    last_prime = primes[-1]
    for j in range(i,prime_len):
        s += primes[j]
        if s> last_prime:
            break
        if s in prime_set:
            largest_prime = (j-i+1,s)
    return largest_prime
        
def consecutive_prime_sum(max_n):
    primes = list(primerange(2,max_n))
    prime_set = set(primes)
    
    prime_len = len(primes)
    max_prime = (0,-1)
    for i in range(prime_len):
        max_p = get_largest_consecutive(primes, prime_set,i)
        if max_p[0]> max_prime[0]:
            max_prime = max_p
        if max_prime[0]> prime_len -i +1:
            break
    
    return max_prime[1]
        

if __name__ == "__main__":     
    start = time.clock()   
    print(consecutive_prime_sum(1000000))
    end = time.clock()
    print("It took ",end - start," seconds")
    