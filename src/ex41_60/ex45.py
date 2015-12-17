import time

def triangle_num(n):
    return n*(n+1)/2

def pentagonal_num(n):
    return n*(3*n - 1)/2

def hexagonal_num(n):
    return n*(2*n - 1)

def find_second_equality():
    counter = 0
    i,j,k = 1,1,1
    n1, n2,n3 = 1,1,1
    while n1<= n2:
        i +=1
        n1 = triangle_num(i)
        while n2 < n1:
            j +=1
            n2 = pentagonal_num(j)
        if n2 == n1:
            while n3 < n2:
                k += 1
                n3 = hexagonal_num(k)
                if n2 == n3:
                    counter +=1
                    if counter ==2:
                        return n3


            
    
if __name__ == "__main__":     
    start = time.clock()   
    print(find_second_equality())
    end = time.clock()
    print("It took ",end - start," seconds")
                         