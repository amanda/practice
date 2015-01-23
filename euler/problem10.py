def sieve_of_eratosthenes(maximum):
    sieve = {i: True for i in range(2, maximum)}
    for n in range(2, maximum):
        if not sieve[n]:
            continue
        yield n
        for i in range(n**2, maximum, n):
        	sieve[i] = False

def sum_of_primes(n):
	return sum(list(sieve_of_eratosthenes(n)))

if __name__ == '__main__':
	print sum_of_primes(2000000)