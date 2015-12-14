import time
from sympy import Rational

def cancel_digit_fractions():
    pRational = Rational(1,1)
    for i in range(1,10):
        for j in range(i+1,10):
            r1 = Rational(i,j)
            for k in range(1,10):
                a_arr = [10*k + i, 10*i+k]
                b_arr = [10*k + j, 10*j+k]
                for a in a_arr:
                    for b in b_arr:
                        if b>a:
                            r2 = Rational(a,b)
                            if r1 == r2:
                                pRational = pRational *r1
    return pRational.q


if __name__ == "__main__":     
    start = time.clock()   
    print(cancel_digit_fractions())
    end = time.clock()
    print("It took ",end - start," seconds")    
                                
                            
                