from itertools import count
import time
def permuted_multiples(n):
    for i in count(1):
        num_gen = (i*j for j in range(1,n+1))
        str_gen = ("".join(sorted(str(num))) for num in num_gen)
        if len(set(str_gen)) ==1:
            return i
        
if __name__ == "__main__":     
    start = time.clock()   
    print(permuted_multiples(6))
    end = time.clock()
    print("It took ",end - start," seconds") 
    