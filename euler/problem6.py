def square_sum_difference(n):
	return sum(range(1, n+1)) ** 2 - sum(i**2 for i in range(1, n+1))

if __name__ == '__main__':
	print square_sum_difference(100)