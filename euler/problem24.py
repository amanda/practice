import itertools

def get_permutations(num_list):
	permutations = list(itertools.permutations(num_list))
	return permutations

if __name__ == '__main__':
	permutation = get_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[999999]
	print ''.join(str(i) for i in permutation)
