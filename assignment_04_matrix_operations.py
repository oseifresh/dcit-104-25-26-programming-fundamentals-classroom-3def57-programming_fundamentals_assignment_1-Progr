# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
"""
Matrix Operations Assignment

Implements three parts:
A) Transpose a matrix
B) Add two matrices
C) Multiply two matrices

All operations use nested loops and are implemented in separate functions.
"""

def read_int(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Please enter a valid integer.")


def read_matrix(rows, cols):
	matrix = []
	for r in range(rows):
		while True:
			row_input = input(f"Enter row {r+1}: ").strip().split()
			if len(row_input) != cols:
				print(f"Please enter exactly {cols} values.")
				continue
			try:
				row = [int(x) for x in row_input]
				matrix.append(row)
				break
			except ValueError:
				print("Please enter integer values only.")
	return matrix


def print_matrix(matrix):
	if not matrix:
		print("[]")
		return
	# determine column widths
	cols = len(matrix[0])
	widths = [0] * cols
	for r in matrix:
		for c in range(cols):
			widths[c] = max(widths[c], len(str(r[c])))
	for r in matrix:
		line = " ".join(str(r[c]).rjust(widths[c]) for c in range(cols))
		print(line)


def transpose_matrix(matrix):
	if not matrix:
		return []
	rows = len(matrix)
	cols = len(matrix[0])
	result = [[0 for _ in range(rows)] for _ in range(cols)]
	for i in range(rows):
		for j in range(cols):
			result[j][i] = matrix[i][j]
	return result


def add_matrices(a, b):
	rows = len(a)
	cols = len(a[0])
	result = [[0 for _ in range(cols)] for _ in range(rows)]
	for i in range(rows):
		for j in range(cols):
			result[i][j] = a[i][j] + b[i][j]
	return result


def multiply_matrices(a, b):
	m = len(a)
	n = len(a[0])  # also rows of b
	p = len(b[0])
	# initialize result m x p with zeros
	result = [[0 for _ in range(p)] for _ in range(m)]
	for i in range(m):
		for j in range(p):
			sum_val = 0
			for k in range(n):
				sum_val += a[i][k] * b[k][j]
			result[i][j] = sum_val
	return result


def part_a():
	print("PART A — Transpose a Matrix")
	r = read_int("Enter number of rows: ")
	c = read_int("Enter number of columns: ")
	mat = read_matrix(r, c)
	print("Original Matrix:")
	print_matrix(mat)
	trans = transpose_matrix(mat)
	print("Transposed Matrix:")
	print_matrix(trans)


def part_b():
	print("PART B — Add Two Matrices")
	r = read_int("Enter number of rows: ")
	c = read_int("Enter number of columns: ")
	print("Matrix A:")
	a = read_matrix(r, c)
	print("Matrix B:")
	b = read_matrix(r, c)
	print("Sum (A + B):")
	print_matrix(add_matrices(a, b))


def part_c():
	print("PART C — Multiply Two Matrices")
	m = read_int("Enter number of rows for matrix A: ")
	n = read_int("Enter number of columns for matrix A (and rows for B): ")
	p = read_int("Enter number of columns for matrix B: ")
	print("Matrix A:")
	a = read_matrix(m, n)
	print("Matrix B:")
	b = read_matrix(n, p)
	print("Product (A x B):")
	print_matrix(multiply_matrices(a, b))


def main():
	part_a()
	print()
	part_b()
	print()
	part_c()


if __name__ == "__main__":
	main()



