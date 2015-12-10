import time

"""
Stupid documentation
"""

def max_reciprocal_cycle_length():
    reciprocal_generator = (reciprocal_cycle_length(i) for i in range(2,1000))
    res = max(reciprocal_generator)
    return res

def reciprocal_cycle_length(n):
    quotients = {}
    m = 10
    counter =0
    while m>0:
        if m in quotients:
            return counter - quotients[m]  
        quotients[m] = counter
        m = 10*(m%n)
        counter +=1
    return 0
        
    
if __name__ == "__main__":
	start = time.clock()
	print(max_reciprocal_cycle_length())
	end = time.clock()
	print("It took ",end - start," seconds")

          
    