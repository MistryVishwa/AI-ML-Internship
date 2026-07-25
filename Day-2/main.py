"""
=========================================================
Python Basics Toolkit
Codomax Digital Solutions Internship
Day 2 Task
=========================================================
Concepts Covered:
✔ Variables
✔ Data Types
✔ Operators
✔ Conditional Statements
✔ Loops
✔ Functions
✔ Modular Programming
=========================================================
"""

from utils.calculator import calculator
from utils.number_operations import even_odd, largest_number
from utils.loops_demo import multiplication_table, factorial, sum_of_numbers
from utils.functions_demo import greet_user
from utils.data_types_demo import show_data_types


def menu():

    while True:

        print("\n" + "=" * 50)
        print(" PYTHON BASICS TOOLKIT ")
        print("=" * 50)

        print("1. Show Data Types")
        print("2. Calculator")
        print("3. Even / Odd Checker")
        print("4. Multiplication Table")
        print("5. Factorial")
        print("6. Sum of First N Numbers")
        print("7. Largest of Three Numbers")
        print("8. Greeting Function")
        print("9. Exit")

        choice = input("\nEnter your choice : ")

        if choice == "1":
            show_data_types()

        elif choice == "2":
            calculator()

        elif choice == "3":
            even_odd()

        elif choice == "4":
            multiplication_table()

        elif choice == "5":
            factorial()

        elif choice == "6":
            sum_of_numbers()

        elif choice == "7":
            largest_number()

        elif choice == "8":
            greet_user()

        elif choice == "9":
            print("\nThank you for using Python Basics Toolkit.")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    menu()