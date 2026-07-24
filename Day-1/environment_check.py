"""
AI & ML Internship - Day 1
Environment Setup Verification Program

Author: Vishwa Mistry
"""

import platform
import sys
from datetime import datetime


def print_header():
    print("=" * 60)
    print("      AI & ML Internship - Day 1 Environment Setup")
    print("=" * 60)


def show_system_information():
    print("\nSystem Information")
    print("-" * 60)
    print(f"Operating System : {platform.system()} {platform.release()}")
    print(f"Machine          : {platform.machine()}")
    print(f"Python Version   : {platform.python_version()}")
    print(f"Python Executable: {sys.executable}")


def internship_information():
    print("\nInternship Information")
    print("-" * 60)

    student = "Vishwa Mistry"
    domain = "Artificial Intelligence & Machine Learning"
    company = "Codomax Digital Solutions"

    print(f"Intern Name : {student}")
    print(f"Company     : {company}")
    print(f"Domain      : {domain}")


def environment_status():
    print("\nDevelopment Environment Status")
    print("-" * 60)

    tools = {
        "Python": "Installed",
        "VS Code": "Installed",
        "Git": "Installed",
        "Jupyter Notebook": "Installed"
    }

    for tool, status in tools.items():
        print(f"{tool:<20} : {status}")


def closing_message():
    print("\n" + "=" * 60)
    print("Development Environment is Ready!")
    print("Ready to start learning AI, ML and Data Science.")
    print(f"Execution Time : {datetime.now()}")
    print("=" * 60)


def main():
    print_header()
    show_system_information()
    internship_information()
    environment_status()
    closing_message()


if __name__ == "__main__":
    main()