import time

def name_scores():
	f = open('p022_names.txt', 'r')
	names = f.read().split(",")
	sorted_names = sorted(map(lambda x: x[1:-1], names))
	
	total = 0
	for i,name in enumerate(sorted_names):
		total +=  (i+1) * sum(map(lambda x: ord(x)- ord('A') + 1, name))
	return total

start = time.clock()
res = name_scores()
end = time.clock()
print(res)
print("It took ",end - start," seconds")