# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#

def print_table(n: int) -> None:
	"""Print multiplication table for n from 1 to 12."""
	print(f"Multiplication Table for {n}:")
	for i in range(1, 13):
		print(f"{n}  x  {i}  =  {n * i}")


def print_tables_to_n(N: int) -> None:
	"""Print multiplication tables for 1..N, separated by a line."""
	for num in range(1, N + 1):
		print_table(num)
		if num != N:
			print("---------------------------")


def get_positive_int(prompt: str) -> int:
	try:
		val = int(input(prompt))
		if val <= 0:
			raise ValueError
		return val
	except Exception:
		print("Error: N must be a positive integer.")
		raise


def main() -> None:
	# Part A — Single Table
	try:
		n = get_positive_int("Enter a number for a single table: ")
	except Exception:
		return
	print_table(n)

	# Part B — Tables from 1 to N (bonus)
	try:
		N = get_positive_int("Enter N to print tables from 1 to N: ")
	except Exception:
		return
	print_tables_to_n(N)


if __name__ == "__main__":
	main()

