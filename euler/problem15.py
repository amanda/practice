def make_coordinates(size):
	for i in range(size + 1):
		for j in range(size + 1):
			yield i, j

def lattice(size):
	coordinates = {}
	for x, y in make_coordinates(size):
		if x == 0 or y == 0:
			coordinates[x, y] = 1
		else:
			coordinates[x, y] = coordinates[x, y-1] + coordinates[x-1, y]
	return coordinates[size, size]

if __name__ == '__main__':
	print lattice(20)
