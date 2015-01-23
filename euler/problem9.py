def pyth_triplets(n):
    for x in xrange(1, n):
        for y in xrange(x+1, n):
            z = x * x + y * y
            sqrt_z = int(z**.5)
            if sqrt_z*sqrt_z == z:
                if x + y + sqrt_z == 1000:
                	return x * y * sqrt_z


if __name__ == '__main__':
	print pyth_triplets(1000)