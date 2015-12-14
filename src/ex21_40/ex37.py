from sympy import nextprime, isprime
import time

def truncatables_primes():
    count =0
    s = 0
    last_prime = 7
    while count<11:
        prime = nextprime(last_prime)
        prime_str = str(prime)
        is_cool = True
        for i in range(1,len(prime_str)):
            p1 = int(prime_str[i:])
            p2 = int(prime_str[:-i])
            if not (isprime(p1) and isprime(p2)):
                is_cool = False
        if is_cool:
            count = count +1
            s = s+prime
        last_prime = prime
    return s
            
if __name__ == "__main__":     
    start = time.clock()   
    print(truncatables_primes())
    end = time.clock()
    print("It took ",end - start," seconds")             