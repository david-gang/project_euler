import time
import math

def lexographic_permutation(n,index):
    index = index-1
    initial_arr = list(range(n))
    counter = math.factorial(n-1)
    perms = []
    for i in range(n-1,0,-1):
        index, j = index%counter, index//counter
        perms.append(initial_arr.pop(j))
        counter = counter//i
    perms.append(initial_arr[0])
    return "".join(map(str,perms))
    

if __name__ == "__main__":
	start = time.clock()
	res = lexographic_permutation(10,10**6)
	end = time.clock()
	print(res)
	print("It took ",end - start," seconds")

          
    