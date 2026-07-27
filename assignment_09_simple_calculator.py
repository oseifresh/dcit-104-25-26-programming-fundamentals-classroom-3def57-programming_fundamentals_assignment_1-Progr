# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# 
#
def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return round(a / b, 2)


def modulus_numbers(a, b):
    return a % b


def exponentiate_numbers(a, b):
    return a ** b


def get_numbers():
    while True:
        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
            return first_number, second_number
        except ValueError:
            print("Error: Please enter valid numbers.")


def main():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

    while True:
        choice = input("Select an operation (1-7): ").strip()

        if choice == "1":
            num1, num2 = get_numbers()
            result = add_numbers(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            num1, num2 = get_numbers()
            result = subtract_numbers(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            num1, num2 = get_numbers()
            result = multiply_numbers(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == "4":
            num1, num2 = get_numbers()
            try:
                result = divide_numbers(num1, num2)
            except ZeroDivisionError as error:
                print(f"Error: {error}")
            else:
                print(f"Result: {num1} / {num2} = {result:.2f}")
        elif choice == "5":
            num1, num2 = get_numbers()
            result = modulus_numbers(num1, num2)
            print(f"Result: {num1} % {num2} = {result}")
        elif choice == "6":
            num1, num2 = get_numbers()
            result = exponentiate_numbers(num1, num2)
            print(f"Result: {num1} ** {num2} = {result}")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid selection. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()

