import time
import os

def name_scores():
	file = os.path.join(os.path.dirname(__file__), 'p022_names.txt')
	f = open(file, 'r')
	names = f.read().split(",")
	f.close()
	sorted_names = sorted(map(lambda x: x[1:-1], names))
	
	total = 0
	for i,name in enumerate(sorted_names):
		total +=  (i+1) * sum(map(lambda x: ord(x)- ord('A') + 1, name))
	return total
