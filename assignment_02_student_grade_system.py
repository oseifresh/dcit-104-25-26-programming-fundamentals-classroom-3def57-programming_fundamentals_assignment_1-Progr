# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 2
# Topic: Conditional Logic (if / elif / else) and Functions
# =============================================================================
#
# TASK: Student Grade System
#
# Write a Python program that reads a student's score and outputs the
# corresponding letter grade based on the scale below.
#
# Grading Scale:
#   Score 80 – 100  →  Grade A
#   Score 70 – 79   →  Grade B
#   Score 60 – 69   →  Grade C
#   Score 50 – 59   →  Grade D
#   Score below 50  →  Grade F
#
grade = float(input("Enter your grade (0-100): "))
if grade >= 80:
    print("Grade: A")
elif grade >= 70:
    print("Grade: B")
elif grade >= 60:
    print("Grade: C")
elif grade >= 50:
    print("Grade: D")
else:
    print("Grade: F")



