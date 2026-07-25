"""
Calculator Module
Demonstrates arithmetic operators.
"""


def calculator():

    try:

        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number : "))

        print("\nOperations")

        print("Addition :", num1 + num2)
        print("Subtraction :", num1 - num2)
        print("Multiplication :", num1 * num2)

        if num2 != 0:
            print("Division :", num1 / num2)
            print("Floor Division :", num1 // num2)
            print("Modulus :", num1 % num2)

        else:
            print("Division by zero not allowed.")

        print("Power :", num1 ** num2)

    except ValueError:
        print("Please enter valid numbers.")