import time
def champernownes_constant():
   interesting_digits = [10, 100, 1000, 10000, 100000, 1000000]
   interesting_index = 0
   counter = 0
   index = 0
   interesting_digit = interesting_digits[interesting_index]
   res = 1
   while interesting_index < len(interesting_digits):
       counter += 1
       num_char = str(counter)
       next_index = index + len(num_char)
       if index < interesting_digit and interesting_digit <= next_index:
           n = int(num_char[interesting_digit -1 - index])
           res = res * n
           interesting_index = interesting_index + 1
           if interesting_index < len(interesting_digits):
               interesting_digit = interesting_digits[interesting_index]
       index = next_index
   return res
           
       

if __name__ == "__main__":     
    start = time.clock()   
    print(champernownes_constant())
    end = time.clock()
    print("It took ", end - start, " seconds") 
