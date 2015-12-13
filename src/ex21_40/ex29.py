from sympy import factorint
import time

def distinct_powers(max_a,max_b):
    power_set = set()
    for a in range(2, max_a+1):
        prime_factors = sorted(factorint(a).items())
        power_primes = list(prime_factors)
        for b in range(2, max_b +1):
            power_primes = [(z[0][0], z[0][1] + z[1][1]) for z in zip(power_primes, prime_factors)]
            power_representation = ",".join('{}:{}'.format(p[0],p[1]) for p in power_primes)
            power_set.add(power_representation)
    return len(power_set)
            
        
if __name__ == "__main__":     
    start = time.clock()   
    print(distinct_powers(100,100))
    end = time.clock()
    print("It took ",end - start," seconds")