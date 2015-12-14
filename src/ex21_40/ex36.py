import time

def is_palindrom(n):
    d = len(n)
    if d==1:
        return True
    e = d//2
    left = n[:e]
    right = n[:(-e-1):-1]
    return  (left[0]) != '0' and (right[0] != '0') and (left == right) 
    

def decimal_and_binary_palindrom():
    s =0
    for n in range(1,1000000):
        if is_palindrom(str(n)):
            binary_str = bin(n)[2:]
            if is_palindrom(binary_str):
                s = s+n
    return s

if __name__ == "__main__":     
    start = time.clock()   
    print(decimal_and_binary_palindrom())
    end = time.clock()
    print("It took ",end - start," seconds")    