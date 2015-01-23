class Deque(object):
	def __init__(self):
		self.items = []
	def __iter__(self):
		for i in self.items:
			yield i
	def add_to_front(self, item):
		self.items.append(item)
	def add_to_back(self, item):
		self.items.insert(0, item)
	def remove_from_front(self):
		return self.items.pop()
	def remove_from_back(self):
		return self.items.pop(0)
	def is_empty(self):
		return self.items == []
	def size(self):
		return len(list(self))

def is_palindrome(a_string):
	d = Deque()
	is_palindrome = True

	if a_string == '':
		is_palindrome = False

	for l in a_string:
			d.add_to_back(l)

	while is_palindrome and d.size() > 1:
		first = d.remove_from_front()
		last = d.remove_from_back()
		if first != last:
			is_palindrome = False
	
	return is_palindrome
