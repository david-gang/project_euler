from sympy import primefactors
import time

def p_fact(n):
    return (n,len(primefactors(n)))
def find_consecutive(n):
    arr = [p_fact(i) for i in range(2,2+n)]
    counter = 2+n-1
    while True:
        if all(a[1]==n for a in arr):
            return arr[0][0]
        counter +=1
        arr.pop(0)
        arr.append(p_fact(counter))
    
    

    
if __name__ == "__main__":     
    start = time.clock()   
    print(find_consecutive(4))
    end = time.clock()
    print("It took ",end - start," seconds")