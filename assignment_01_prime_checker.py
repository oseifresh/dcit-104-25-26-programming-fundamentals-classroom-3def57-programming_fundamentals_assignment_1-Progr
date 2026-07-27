# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
#
# Write a Python program that checks whether a given number is prime.
#
# Function to check if a number is prime
def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False

    # Check for factors from 2 to number - 1
    for i in range(2, number):
        if number % i == 0:
            return False

    return True
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")


