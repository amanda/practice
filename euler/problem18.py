problem_triangle = [[75],
			[95, 64],
			[17, 47, 82],
			[18, 35, 87, 10],
			[20, 04, 82, 47, 65],
			[19, 01, 23, 75, 03, 34],
			[88, 02, 77, 73, 07, 63, 67],
			[99, 65, 04, 28, 06, 16, 70, 92],
			[41, 41, 26, 56, 83, 40, 80, 70, 33],
			[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
			[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
			[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
			[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
			[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
			[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]

# problem_triangle = [[3],
# 			[7, 4],
# 			[2, 4, 6],
# 			[8, 5, 9, 3]]

# problem_triangle = [[1], [2, 3], [4, 5, 6]]

def go_through_rows(triangle):
	for i in range(len(triangle) - 1, 0, -1):
		current_row = triangle[i]
		above_row = triangle[i - 1]
		for j in range(len(above_row)):
			if current_row[j] > current_row[j + 1]:
				above_row[j] = current_row[j] + above_row[j]
			else:
				above_row[j] = current_row[j + 1] + above_row[j]
	return triangle[0]

if __name__ == '__main__':
	print go_through_rows(problem_triangle)

