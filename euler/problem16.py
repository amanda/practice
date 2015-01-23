def sum_of_digits(power):
	number = 2**power
	stringy_number = str(number)
	numbery_list = map(int, stringy_number)
	return sum(numbery_list)

if __name__ == '__main__':
	print sum_of_digits(1000)