import itertools

def gen_proper_divisors(n):
	yield 1
	for i in range(2, n):
		if n % i == 0:
			yield i

def find_abundants(maximum):
	for i in range(1, maximum + 1):
		if sum(gen_proper_divisors(i)) > i:
			yield i

def non_abundant_sum(maximum):
	abundants = list(find_abundants(maximum))
	pairs = itertools.product(abundants, abundants)
	abundant_dict = {d:0 for d in range(maximum + 1)}

	for pair in pairs:
		summed = sum(pair)
		if summed <= maximum:
			abundant_dict[summed] += 1

	return sum(k for k, v in abundant_dict.iteritems() if v == 0)

if __name__ == '__main__':
	print non_abundant_sum(28123)
