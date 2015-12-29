import time
from sympy import binomial

def count_cnr_bigger(n,min_n):
    bin_gen = (binomial(i,j) for i in range(1,n+1) for j in range(1,i+1))
    return sum(1 for x in bin_gen if x> min_n)

if __name__ == "__main__":     
    start = time.clock()   
    print(count_cnr_bigger(100,10**6))
    end = time.clock()
    print("It took ",end - start," seconds") 