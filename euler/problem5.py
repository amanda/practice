from collections import Counter

def prime_factors(n):
	for i in range(2, n+1):
		while n%i == 0:
			yield i
			n /= i

def most_frequent(x,y):
    all_keys = set(x.keys()) | set(y.keys())
    z = {}
    for k in all_keys:
        z[k] = max(x.get(k,0),y.get(k,0))
    return z

def find_smallest_divisible(n):
	factor_dicts = map(Counter,map(prime_factors,range(1,n+1)))
	frequent_factors = reduce(most_frequent,factor_dicts)
	raised = [a**b for a,b in frequent_factors.items()]
	return reduce(lambda x,y: x*y,raised)

if __name__ == '__main__':
	print find_smallest_divisible(20)