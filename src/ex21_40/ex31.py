import time
coin_arr = [200, 100, 50, 20, 10, 5, 2, 1]

def _coin_sums(n, i):
    if n==0:
        return 1
    if i == len(coin_arr) -1:
        return 1
    
    m = coin_arr[i]
    return sum( _coin_sums(n -j*m, i+1) for j in range(0, n//m +1))

def coin_sums(n):
    return _coin_sums(n, 0)
        
if __name__ == "__main__":     
    start = time.clock()   
    print(coin_sums(200))
    end = time.clock()
    print("It took ",end - start," seconds")