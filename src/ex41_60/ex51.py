from itertools import count, dropwhile, product
from sympy import primerange
import time

def get_star_perms(num_str):
    num_dict = {}
    for (i,num) in enumerate(num_str):
        if num in num_dict:
            num_dict[num].append(i)
        else:
            num_dict[num] = [i]   
    for entry in num_dict.items():
        bool_perms = ([False, True] for _ in range(len(entry[1])))
        bool_gen = product(*bool_perms)
        next(bool_gen)
        for bool_comb in bool_gen:
            num_key = list(num_str)
            for x in zip(bool_comb,entry[1]):
                if x[0]:
                    num_key[x[1]] = '*'
            
            yield "".join(num_key)
             
        
def prime_digit_replacements_of(number_of_primes,n):
    primes = primerange(10**(n-1), 10**n)
    rep_dict = {}
    for p in primes:
        p_str = str(p)
        for perm in get_star_perms(p_str):
            if perm not in rep_dict:
                rep_dict[perm] = [p,1]
            else:
                rep_dict[perm][1]+=1
    num_filter = (v for v in rep_dict.values() if v[1] == number_of_primes)
    nums = sorted(num_filter)
    if len(nums):
        return nums[0][0]
    else:
        return None
        
    

def prime_digit_replacements(number_of_primes):
    prime_digit_gen =  (prime_digit_replacements_of(number_of_primes,n) for n in count(2))
    prime_digit_gen2 = dropwhile(lambda x: x==None, prime_digit_gen)
    return next(prime_digit_gen2)

if __name__ == "__main__":     
    start = time.clock()   
    print(prime_digit_replacements(8))
    end = time.clock()
    print("It took ",end - start," seconds") 
    