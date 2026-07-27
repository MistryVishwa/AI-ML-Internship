import numpy as np


def statistics_demo():

    print("\n" + "=" * 60)
    print("STATISTICAL FUNCTIONS")
    print("=" * 60)

    marks = np.array([72, 85, 96, 68, 77, 89])

    print("Marks")

    print(marks)

    print("\nSum")

    print(np.sum(marks))

    print("\nAverage")

    print(np.mean(marks))

    print("\nMedian")

    print(np.median(marks))

    print("\nMaximum")

    print(np.max(marks))

    print("\nMinimum")

    print(np.min(marks))

    print("\nVariance")

    print(np.var(marks))

    print("\nStandard Deviation")

    print(np.std(marks))