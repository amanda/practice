def merge(left, right):
	result = [0] * len(left + right)
	i, j, x = 0, 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result[x] = left[i]
			i += 1
		else:
			result[x] = right[j]
			j += 1
		x += 1
	while i < len(left):
		result[x] = left[i]
		i +=1
		x += 1
	while j < len(right):
		result[x] = right[j]
		j += 1
		x += 1
	return result

def merge_sort(a):
	if len(a) == 1:
		return a
	mid = len(a)/2
	return merge(merge_sort(a[mid:]), merge_sort(a[:mid]))
