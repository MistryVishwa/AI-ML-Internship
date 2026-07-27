import numpy as np


def mathematics_demo():

    print("\n" + "=" * 60)
    print("MATHEMATICAL OPERATIONS")
    print("=" * 60)

    a = np.array([10, 20, 30])

    b = np.array([2, 5, 10])

    print("A =", a)

    print("B =", b)

    print("\nAddition")

    print(a + b)

    print("\nSubtraction")

    print(a - b)

    print("\nMultiplication")

    print(a * b)

    print("\nDivision")

    print(a / b)

    print("\nSquare")

    print(np.square(a))

    print("\nSquare Root")

    print(np.sqrt(a))

    print("\nPower")

    print(np.power(a, 2))

    print("\nAbsolute")

    print(np.abs([-10, -20, 5]))