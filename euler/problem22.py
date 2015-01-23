from sys import argv

VALUES = {
	'A': 1, 
	'B': 2,
	'C': 3,
	'D': 4,
	'E': 5,
	'F': 6, 
	'G': 7,
	'H': 8,
	'I': 9,
	'J': 10,
	'K': 11,
	'L': 12,
	'M': 13,
	'N': 14,
	'O': 15,
	'P': 16,
	'Q': 17,
	'R': 18,
	'S': 19,
	'T': 20,
	'U': 21,
	'V': 22, 
	'W': 23,
	'X': 24,
	'Y': 25,
	'Z': 26
}

def name_value(name):
	listy_name = list(name)
	values = []
	for letter in listy_name:
		value = VALUES[letter]
		values.append(value)
	return sum(values)

def total_name_score(all_names):
	for i, name in enumerate(sorted(all_names), start=1):
		yield i * name_value(name)

with open(argv[1]) as f:
	words = f.read().replace('"', '').split(',')
	print sum(total_name_score(words))
