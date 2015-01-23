def is_palindrome(n):
	return str(n) == ''.join(reversed(str(n)))

def get_multiples(start_range, end_range):
	return ((i*x) for i in xrange(start_range,end_range) for x in xrange(i,end_range))

if __name__ == '__main__':
	print max(filter(is_palindrome,get_multiples(100,1000)))