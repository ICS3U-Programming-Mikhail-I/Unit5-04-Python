# Author: 2025 Mikhail Ibrahim
# Date: May 19th, 2025
# Description: A crash-proof calculator program that accepts an operation symbol
# and two float numbers from the user. It validates input and performs the
# corresponding calculation using a function.


def calculate(sign, first_number, second_number):
    """
    Perform the arithmetic operation based on the sign.
    Return the result or an error message.
    """
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "*":
        return first_number * second_number
    elif sign == "/":
        if second_number != 0:
            return first_number / second_number
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"


def main():
    print("Welcome to the Basic Calculator")

    try:
        sign = input("Enter operation (+, -, *, /): ").strip()
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        result = calculate(sign, first, second)

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
