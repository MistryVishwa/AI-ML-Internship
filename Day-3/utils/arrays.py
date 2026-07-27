import numpy as np


def arrays_demo():

    print("\n" + "=" * 60)
    print("NUMPY ARRAY CREATION")
    print("=" * 60)

    one_d = np.array([10, 20, 30, 40, 50])

    print("\n1D Array")
    print(one_d)

    two_d = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    print("\n2D Array")
    print(two_d)

    print("\nArray Information")

    print("Shape :", two_d.shape)
    print("Dimension :", two_d.ndim)
    print("Size :", two_d.size)
    print("Data Type :", two_d.dtype)

    zeros = np.zeros((3, 3))

    print("\nZeros Matrix")
    print(zeros)

    ones = np.ones((2, 4))

    print("\nOnes Matrix")
    print(ones)

    sequence = np.arange(1, 11)

    print("\nSequence")
    print(sequence)

    evenly = np.linspace(0, 100, 5)

    print("\nLinspace")
    print(evenly)