def sieve_of_eratosthenes(maximum):
    sieve = {i: True for i in range(2, maximum)}
    for n in range(2, maximum):
        if not sieve[n]:
            continue
        yield n
        for i in range(n**2, maximum, n):
        	sieve[i] = False

def nth_prime(num, maximum=10**6):
	return next(b for a,b in enumerate(sieve_of_eratosthenes(maximum),1) if a == num)

if __name__ == '__main__':
	print nth_prime(10001)