# Name: Mark Neilson Tol
# Section: IV-BSIT C
# Activity: P3 - Student Record Manager
# Date: November 16, 2026


def add_student(students, name):
    name = name.strip()
    if name == "":
        print("Name cannot be empty.")
        return
    # Compare in lowercase so "Juan Cruz" and "juan cruz" are the same
    for existing in students:
        if existing.lower() == name.lower():
            print(f"{existing} already exists.")
            return
    students.append(name)
    print(f"{name} added.")


def display_students(students):
    if len(students) == 0:
        print("No students yet.")
        return
    # sorted() gives alphabetical order, ignoring upper/lower case
    for number, name in enumerate(sorted(students, key=str.lower), start=1):
        print(f"{number}. {name}")
    print(f"Total: {len(students)}")


def main():
    students = []

    while True:
        print("\n=== Student Record Manager - Mark Neilson Tol ===")
        print("1. Add student")
        print("2. Display all students")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_student(students, input("Enter student name: "))
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()
