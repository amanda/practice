names = ['Mary', 'Isla', 'Sam']
'''
rewrite as a map
for i in range(len(names)):
    names[i] = hash(names[i])

print names
'''
secret_names = map(hash, names)
print secret_names

people = [{'name': 'Mary', 'height': 160},
    {'name': 'Isla', 'height': 80},
    {'name': 'Sam'}]


'''
Exercise 2. Try rewriting the code below using map, reduce and filter. Filter takes a function and a collection. It returns a collection of every item for which the function returned True.
height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1
if height_count > 0:
average_height = height_total / height_count

print average_height
'''
heights = map(lambda x: x['height'], filter(lambda x: 'height' in x, people))
average = sum(heights) / len(heights)


'''
Exercise 4. Try and write the pipeline_each function. Think about the order of operations. The bands in the array are passed, one band at a time, to the first transformation function. The bands in the resulting array are passed, one band at a time, to the second transformation function. And so forth.
'''
bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def set_canada_as_country(band):
    return assoc(band, 'country', "Canada")

def strip_punctuation_from_name(band):
    return assoc(band, 'name', band['name'].replace('.', ''))

def capitalize_names(band):
    return assoc(band, 'name', band['name'].title())

def pipeline_each(group, funcs)
	return reduce(lambda a, x, map(x, a): funcs, group)

print pipeline_each(bands, [set_canada_as_country,
                            strip_punctuation_from_name,
                            capitalize_names])

'''
Exercise 5. pluck() takes a list of keys to extract from each record. Try and write it. It will need to be a higher order function.
'''
def pluck(record):
	def plucking(keys):
		return reduce(lambda a, x: assoc(a, x, record[x]), keys, {})
	return pluckings

