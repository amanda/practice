from collections import defaultdict

def find_proper_divisors(n):
	divisors = [1]
	for i in range(2, n):
		if n % i == 0:
			divisors.append(i)
	return divisors

def sum_amicable_numbers_under(maximum):
	amicables = defaultdict(int)
	
	for sums in ((n, sum(find_proper_divisors(n))) for n in xrange(1, maximum)):
		amicables[tuple(sorted((sums)))] += 1

	return sum(sum(k) for k, v in amicables.iteritems() if v > 1)

if __name__ == '__main__':
	print sum_amicable_numbers_under(10000)
