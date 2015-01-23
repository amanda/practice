fib = [1]

a, b = 1,1
for i in range(100):
	a, b = b, a + b
	fib.append(b)
	if b > 4000000:
		break
		
print sum(x for x in fib if x % 2 == 0)