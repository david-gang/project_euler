import time
from sympy import primerange
from itertools import permutations

def prime_permutations():
    primes = list(primerange(1000,10000))
    prime_set = set(primes)
    checked = set()
    for prime in primes:
        if prime in checked:
            continue
        perm_gen = (int("".join(p)) for p in permutations(str(prime)))
        perms = sorted(set(perm_gen))
        interesting_perms = [p for p in perms if p>=prime and p in prime_set]
        checked.update(interesting_perms)
        perm_len = len(interesting_perms)
        if perm_len <=2:
            continue
        for i in range(perm_len-2):
            for j in range(i+1,perm_len-1):
                a = interesting_perms[i]
                b = interesting_perms[j]
                diff = b -a
                c = b + diff
                if c in interesting_perms and a!=1487:
                    return "".join((str(a), str(b), str(c)))
                
        
    
        
if __name__ == "__main__":     
    start = time.clock()   
    print(prime_permutations())
    end = time.clock()
    print("It took ",end - start," seconds")