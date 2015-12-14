import time
from operator import itemgetter

def integer_right_triangles(p):
    max_p = p**2
    quadrates = [i**2 for i in range(1,p+1)]
    quadrates_dict = {i**2:i for i in range(1,p+1)}
    sols_dict = {}
    for i in range(p -2):
        for j in range(i+1, p-1):
            a = quadrates[i]
            b = quadrates[j]
            c = a+b
            if c > max_p:
                break
            if c in quadrates_dict:
                res = quadrates_dict[c] + i+1 + j+1
                if res >p:
                    break
                if res in sols_dict:
                    sols_dict[res] = sols_dict[res] + 1
                else:
                    sols_dict[res] = 1
    m = max(sols_dict.items(), key = itemgetter(1))
    return m[0]

if __name__ == "__main__":     
    start = time.clock()   
    print(integer_right_triangles(1000))
    end = time.clock()
    print("It took ",end - start," seconds")             
        


            