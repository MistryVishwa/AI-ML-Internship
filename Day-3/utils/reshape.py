import numpy as np


def reshape_demo():

    print("\n" + "=" * 60)
    print("RESHAPING ARRAYS")
    print("=" * 60)

    arr = np.arange(1, 13)

    print("Original")

    print(arr)

    matrix = arr.reshape(3, 4)

    print("\n3 x 4")

    print(matrix)

    print("\nTranspose")

    print(matrix.T)

    print("\nFlatten")

    print(matrix.flatten())