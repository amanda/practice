import unittest

def memoize(f):
	cache = {}
	def inner(*args):
		try:
			return cache[args]
		except KeyError:
			cache[args] = f(*args)
		return cache[args]
	return inner

def collatz_step(n):
	if n == 1:
		raise ValueError()
	if n % 2 == 0:
		return n/2
	else:
		return 3*n + 1

def collatz_maker(n):
	collatz_sequence = [n]
	while n != 1:
		n = collatz_step(n)
		collatz_sequence.append(n)
	return collatz_sequence

@memoize
def collatz_seq(n):
	if n == 1:
		return [1]
	return [n] + collatz_seq(collatz_step(n))

def longest_collatz(maximum=1000000):
	key_function = lambda n : len(collatz_seq(n))
	return max(range(2, 1000000), key = key_function)

class TestCollatzStep(unittest.TestCase):
	def test_even(self):
		self.assertEquals(collatz_step(2), 1)
		self.assertEquals(collatz_step(80), 40)
		self.assertEquals(collatz_step(24), 12)
	def test_odd(self):
		self.assertEquals(collatz_step(3), 10)
		self.assertEquals(collatz_step(33), 100)
		self.assertEquals(collatz_step(17), 52)
	def test_one(self):
		self.assertRaises(ValueError, lambda: collatz_step(1))

class TestCollatzMaker(unittest.TestCase):
	def test_sequence(self):
		self.assertEquals([13, 40, 20, 10, 5, 16, 8, 4, 2, 1], collatz_seq(13))

if __name__ == '__main__':
	print longest_collatz()