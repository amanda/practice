import math

def get_factorial(n): #turns out math has this, ha
	numbers = []
	for i in range(n, 0, -1):
		numbers.append(i)
	factorial = reduce(lambda x, y: x*y, numbers)
	return factorial

def sum_of_digits(a): #from problem 16
	stringy_number = str(a)
	numbery_list = map(int, stringy_number)
	return sum(numbery_list)

if __name__ == '__main__':
	print sum_of_digits(math.factorial(100))