import time



    
def pentagonal_number(n):
    return int((3*n -1)*n/2);


def check_pentagonal_number():
    pen_length = 3000
    pentagonal_numbers = [pentagonal_number(i) for i in range(1,pen_length +1)]
    pen_diff = []
    pentagonal_set = set(pentagonal_numbers)
    for i in range(pen_length-1):
        n1 = pentagonal_numbers[i]
        for j in range(i+1, pen_length):
            n2 = pentagonal_numbers[j]
            if ((n1+n2) in pentagonal_set) and ((n2 -n1) in pentagonal_set):
                pen_diff.append(n2 - n1)
    return min(pen_diff)
            
        
    
if __name__ == "__main__":     
    start = time.clock()   
    print(check_pentagonal_number())
    end = time.clock()
    print("It took ",end - start," seconds")
            
            
        