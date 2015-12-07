import time
import math

bPhi = (1+ math.sqrt(5))/2
sPhi = (1- math.sqrt(5))/2


def fibonacci(n):
    return (math.pow(bPhi,n) - math.pow(sPhi,n))/math.sqrt(5)
    
    
def fibonacci_order_of_magnitude(n):
    return math.ceil((math.log10(math.sqrt(5)) + n -1) / math.log10(bPhi))

if __name__ == "__main__":
	start = time.clock()
	print(fibonacci_order_of_magnitude(1000))
	end = time.clock()
	print("It took ",end - start," seconds")

          
    