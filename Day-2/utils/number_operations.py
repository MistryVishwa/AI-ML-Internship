"""
Conditional Statements Demo
"""


def even_odd():

    number = int(input("Enter Number : "))

    if number % 2 == 0:
        print(number, "is Even")

    else:
        print(number, "is Odd")


def largest_number():

    a = int(input("First Number : "))
    b = int(input("Second Number : "))
    c = int(input("Third Number : "))

    if a >= b and a >= c:
        print("Largest =", a)

    elif b >= c:
        print("Largest =", b)

    else:
        print("Largest =", c)