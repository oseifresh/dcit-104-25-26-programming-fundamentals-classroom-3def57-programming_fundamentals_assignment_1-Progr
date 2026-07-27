# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# =============================================================================
# FUNCTION DEFINITIONS
# =============================================================================

def calculate_sum(numbers):
    """Calculate the sum of numbers in the list."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Calculate the average of numbers in the list."""
    if len(numbers) == 0:
        return 0
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    """Find the maximum value in the list."""
    if len(numbers) == 0:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def find_minimum(numbers):
    """Find the minimum value in the list."""
    if len(numbers) == 0:
        return None
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


# =============================================================================
# MAIN PROGRAM
# =============================================================================

n = int(input("How many numbers? "))

# Validate input
if n <= 0:
    print("Error: Number of elements must be positive.")
else:
    # Read numbers from user
    numbers = []
    for i in range(1, n + 1):
        num = int(input(f"Enter number {i}: "))
        numbers.append(num)
    
    # Calculate statistics
    total_sum = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)
    
    # Display results
    print("\nResults:")
    print(f"Sum:     {total_sum}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

