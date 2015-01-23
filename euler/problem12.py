from itertools import count
import unittest

def triangle_number_generator():
	n = 0
	for x in count(1):
		n += x
		yield n

def get_factors(n):
	factors = {1, n}
	for i in range(2, int(n**.5)):
		if n % i == 0:
			factors.update([i, n / i])
	return factors

def triangle_number_factors(maximum):
	for triangle in triangle_number_generator():
		factors = get_factors(triangle)
		if len(factors) > maximum:
			return triangle

def triangle_number_test_generator():
	return iter((1, 3, 6, 10, 15, 21, 28, 36, 45, 55))


class TriangleNumberTester(unittest.TestCase):
	def test_triangle(self):
		for a, b in zip(triangle_number_test_generator(), triangle_number_generator()):
			self.assertEqual(a, b)

	def test_factors(self):
		self.assertEqual(get_factors(6), {1,2,3,6})
		self.assertEqual(get_factors(1), {1})
		self.assertEqual(get_factors(13), {1, 13})
		self.assertEqual(get_factors(28), {1, 2, 4, 7, 14, 28})
		self.assertEqual(get_factors(21), {1, 3, 7, 21})

#if __name__ == '__main__':
#	unittest.main()

if __name__ == '__main__':
	print triangle_number_factors(500)
