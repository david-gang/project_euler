import time
from itertools import permutations

conditions = (
              ((1,2,3),2),
              ((2,3,4),3),
              ((3,4,5),5),
              ((4,5,6),7),
              ((5,6,7),11),
              ((6,7,8),13),
              ((7,8,9),17),
              );
def divisible_by(perm, cond):
    num = int(''.join(perm[c] for c in cond[0]))
    return (num % cond[1]) ==0
    
    
def substring_divisibiliy_sum():
    s = 0
    for perm in permutations('0123456789'):
        if perm[0] == '0':
            continue
        if all(divisible_by(perm, cond) for cond in conditions):
            s = s+int(''.join(perm))
    return s

if __name__ == "__main__":     
    start = time.clock()   
    print(substring_divisibiliy_sum())
    end = time.clock()
    print("It took ",end - start," seconds")
            
        