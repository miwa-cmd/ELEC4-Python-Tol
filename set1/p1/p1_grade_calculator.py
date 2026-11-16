# Name: Mark Neilson Tol
# Section: IV-BSIT C
# Activity: P1 - Student Grade Calculator
# Date: November 16, 2026

def get_valid_grade():
    while True:
        try:
            grade = float(input("Enter the student's grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Invalid input. Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


result = get_valid_grade()
print("You entered:", result)