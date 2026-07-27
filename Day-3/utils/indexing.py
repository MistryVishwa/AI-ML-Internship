import numpy as np


def indexing_demo():

    print("\n" + "=" * 60)
    print("ARRAY INDEXING")
    print("=" * 60)

    arr = np.array([5, 10, 15, 20, 25, 30])

    print("Array :", arr)

    print("First Element :", arr[0])

    print("Last Element :", arr[-1])

    print("Slice 1:4 :", arr[1:4])

    print("Every Second :", arr[::2])

    matrix = np.array([
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ])

    print("\nMatrix")

    print(matrix)

    print("\nElement (1,2)")
    print(matrix[1, 2])

    print("\nFirst Row")
    print(matrix[0])

    print("\nSecond Column")
    print(matrix[:, 1])

    print("\nLast Column")
    print(matrix[:, -1])