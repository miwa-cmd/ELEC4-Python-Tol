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


def main():
    grades = []

    while True:
        print("\n=== Student Grade Calculator - Mark Neilson Tol ===")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            grades = []
            while True:
                try:
                    count = int(input("How many grades do you want to enter? "))
                    if count > 0:
                        break
                    else:
                        print("Please enter a number greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            for i in range(count):
                print(f"Grade {i + 1} of {count}")
                grades.append(get_valid_grade())
            print("Grades saved.")

        elif choice == "2":
            if len(grades) == 0:
                print("No grades yet. Choose option 1 first.")
            else:
                average = compute_average(grades)
                print(f"\nGrades: {grades}")
                print(f"Average: {average:.2f}")
                print(f"Highest: {get_highest(grades)}")
                print(f"Lowest: {get_lowest(grades)}")
                print(f"Status: {get_status(average)}")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()

# Local vs Global Variable:
# A local variable is made inside a function and can only be used there, like
# grades and average inside main(). A global variable is made outside all functions
# and can be used anywhere. My program has no global variables because I pass
# grades to each function as a parameter.