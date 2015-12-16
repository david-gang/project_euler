import time
import os
import math

def triangle_numbers():
    file = os.path.join(os.path.dirname(__file__), 'p042_words.txt')
    f = open(file, 'r')
    names = f.read().split(",")
    f.close()
    
    total = 0
    for name in map(lambda x: x[1:-1], names):
        gem2 =  2* sum(map(lambda x: ord(x)- ord('A') + 1, name))
        i = int(math.sqrt(gem2))
        j = i +1
        if gem2 == i*j:
            total = total +1   
    return total

if __name__ == "__main__":     
    start = time.clock()   
    print(triangle_numbers())
    end = time.clock()
    print("It took ", end - start, " seconds") 

