import time

def spiral_diagonals_sum(n):
    k = n//2
    return round(16*(k**3)/3 + 10*k**2 +26*k/3 +1); 

if __name__ == "__main__":
	start = time.clock()
	print(spiral_diagonals_sum(1001))
	end = time.clock()
	print("It took ",end - start," seconds")