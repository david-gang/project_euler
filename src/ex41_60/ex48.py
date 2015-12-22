import time

def self_powers(n):
    n = sum(i**i for i in range(1,n+1))
    n_str = str(n)
    return n_str[-10:]

if __name__ == "__main__":     
    start = time.clock()   
    print(self_powers(1000))
    end = time.clock()
    print("It took ",end - start," seconds")