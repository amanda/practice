def fib_contains(digits):
	a, b = 0, 1
	i = 0
	while len(str(a)) < digits:
		a, b = b, a + b
		i += 1
	return i

if __name__ == '__main__':
	print fib_contains(1000)
	