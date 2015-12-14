from itertools import permutations
import time 

def pandigital_products_for(n1,n2):
    n3 = 9 -n1 -n2
    s = set()
    all_nums = list(range(1,10))
    for a_perm in permutations(all_nums, n1):
        a = int("".join(str(x) for x in a_perm))
        b_nums = [b for b in all_nums if b not in a_perm]
        for b_perm in permutations(b_nums, n2):
            b = int("".join(str(x) for x in b_perm))
            c = a*b
            c_str = str(a*b)
            if len(c_str) > n3:
                break
            c_nums = [c for c in b_nums if c not in b_perm]
            c_expected  = "".join(str(x) for x in c_nums)
            c_actual = "".join(sorted(c_str))
            if c_actual == c_expected:
                s.add(c)
    return s
            
            
    
def pandigital_products():
    s = set()
    for n1 in range(1,3):
        n2 = (9 -n1)//2
        s = s | pandigital_products_for(n1,n2)
    return sum(s)
        
        
if __name__ == "__main__":     
    start = time.clock()   
    print(pandigital_products())
    end = time.clock()
    print("It took ",end - start," seconds")    
    