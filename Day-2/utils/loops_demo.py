"""
Loop Demonstration
"""


def multiplication_table():

    number = int(input("Enter Number : "))

    print()

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


def factorial():

    number = int(input("Enter Number : "))

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    print("Factorial =", fact)


def sum_of_numbers():

    number = int(input("Enter Value of N : "))

    total = 0

    for i in range(1, number + 1):
        total += i

    print("Sum =", total)