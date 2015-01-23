num = 600851475143

def largest_prime_factor(n):
	divided = n
	for i in range(2, n+1):
		while divided % i == 0:
			divided = divided/i
		if divided == 1:
			return i
	return n

if __name__ == '__main__':
	print largest_prime_factor(num)
