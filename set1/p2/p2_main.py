# Name: Mark Neilson Tol
# Section: IV-BSIT C
# Activity: P2 - Custom Module
# Date: November 16, 2026

import student_utils                                # style 1: whole module
from student_utils import get_highest, get_lowest   # style 2: specific names
from datetime import datetime                       # built-in module

print("=== Grade Report - Mark Neilson Tol ===")

grades = []
count = int(input("How many grades? "))
for i in range(count):
    grades.append(float(input(f"Grade {i + 1}: ")))

average = student_utils.compute_average(grades)

print("\nGenerated:", datetime.now().strftime("%B %d, %Y %I:%M %p"))
print("Average:", round(average, 2))
print("Highest:", get_highest(grades))
print("Lowest:", get_lowest(grades))
print("Status:", student_utils.get_status(average))