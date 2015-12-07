import time
import itertools
from decimal import *
getcontext().prec = 2000

"""
Stupid documentation
"""

def reciprocal_cycle_length(n):
    print(n)
    right_side = str(Decimal(1)/Decimal(n))[2:]
    to_check_arr = list(right_side)
    to_check = "".join(to_check_arr)
    max_cycle_length_all = 0
    max_cycle_all = ''
    for i in range(0,len(to_check) -1):
        max_cycle_length =0
        max_cycle = ''
        cycle = to_check[i]
        j = i + 1    
        while j<len(to_check) -len(cycle):
            if cycle == to_check[j:j+len(cycle)] and len(cycle) > max_cycle_length:
                if cycle ==max_cycle + max_cycle:
                    break
                max_cycle_length = len(cycle)
                max_cycle = cycle
            cycle = cycle + to_check[j]
            j = j + 1
        if max_cycle_length > max_cycle_length_all:
            max_cycle_length_all = max_cycle_length
            max_cycle_all = max_cycle 
    return max_cycle_length_all        
    
if __name__ == "__main__":
	start = time.clock()
	reciprocal_generator = ((i,Decimal(1)/Decimal(i), reciprocal_cycle_length(i)) for i in range(2,1000))
	res = max(reciprocal_generator, key = lambda x:x[2])
	print(res)
	end = time.clock()
	print("It took ",end - start," seconds")

          
    