import numpy as np


def student_marks_demo():

    print("\n" + "=" * 60)
    print("REAL WORLD EXAMPLE")
    print("=" * 60)

    students = np.array([
        [78, 82, 91],
        [88, 76, 90],
        [65, 70, 80],
        [95, 91, 89],
        [84, 79, 85]
    ])

    print("Student Marks")

    print(students)

    print("\nAverage of each Student")

    print(np.mean(students, axis=1))

    print("\nAverage of each Subject")

    print(np.mean(students, axis=0))

    print("\nHighest Marks")

    print(np.max(students))

    print("\nLowest Marks")

    print(np.min(students))

    print("\nTotal Marks")

    print(np.sum(students, axis=1))

    grades = np.where(np.mean(students, axis=1) >= 80, "Pass", "Needs Improvement")

    print("\nPerformance")

    print(grades)