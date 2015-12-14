import time
def pandigital_multiples():
    max_pan = 0
    for n in range(1, 10000):
        pan_arr = []
        is_pan = True
        n1 =0
        while True:
            n1 = n1 +n
            for c in str(n1):
                if  (c== '0') or (c in pan_arr):
                    is_pan = False
                pan_arr.append(c)
            
            pan_len = len(pan_arr)    
            if  pan_len == 9:
                break
            
            if pan_len > 9:
                is_pan = False
                break
        if is_pan:
            pan_num = int("".join(pan_arr))
            max_pan = max(max_pan, pan_num)
    return max_pan

if __name__ == "__main__":     
    start = time.clock()   
    print(pandigital_multiples())
    end = time.clock()
    print("It took ",end - start," seconds")             
        
        