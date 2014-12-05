import time
import matplotlib
from matplotlib import pyplot

class Mapping:
	def __init__(self):
		self.data = []
	def add_pair(self, key, value):
		self.data.append([key, value])
	def get_value(self, key):
		counter = 0
		for d in self.data:
			counter += 1
			if d[0] == key:
				return d[1]
		return None
	def remove_entry(self, key):
		for d in self.data:
			if d == key:
				self.data.remove(d)

class ButTheresAlreadyADict:
	def __init__(self):
		self.dict = {}
	def add_pair(self, key, value):
		self.dict[key] = value
	def get_value(self, key):
		return self.dict[key]
	def remove_entry(self, key):
		del self.dict[key]

def make_map(keys):
	my_map = Mapping()
	for i in range(keys):
		my_map.add_pair(i, "hi")
	return my_map

def make_dict(keys):
	my_dict = ButTheresAlreadyADict()
	for i in range(keys):
		my_dict.add_pair(i, "hi")
	return my_dict

#10000 lookups on maps with various number of keys
def map_timer(keys):
	my_map = make_map(keys)
	start = time.time()
	for i in range(10000):
		my_map.get_value(i % keys)
	end = time.time()
	total = end - start
	return total

def dict_timer(keys):
	my_dict = make_dict(keys)
	start = time.time()
	for i in range(10000):
		my_dict.get_value(i % keys)
	end = time.time()
	total = end - start
	return total

if __name__ == '__main__':
	keys = [10, 50, 100, 1000, 10000]
	slow_mapping = [] #time
	regular_old_dict = [] #time
	for k in keys:
		slow_mapping.append(map_timer(k))
		regular_old_dict.append(dict_timer(k))
	pyplot.plot(keys, slow_mapping, 'o')
	pyplot.plot(keys, regular_old_dict, '^')
	pyplot.ylabel('time')
	pyplot.show()
	