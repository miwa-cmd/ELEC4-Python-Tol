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


def compute_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(average):
    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"

print(get_status(80))
print(get_status(74.9))
print(get_status(75))