from sympy import isprime
import math
import time

def golbach_other():
    i = 7
    while True:
        i = i+2
        if isprime(i):
            continue
        max_j = int(math.sqrt(i/2))
        g = False
        for j in range(1,max_j+1):
            if isprime(i - 2*j*j):
                g = True
                break
        if not g:
            return i
        

            
     
if __name__ == "__main__":     
    start = time.clock()   
    print(golbach_other())
    end = time.clock()
    print("It took ",end - start," seconds")   