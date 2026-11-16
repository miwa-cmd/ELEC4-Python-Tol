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


def remove_student(students, name):
    name = name.strip().lower()
    for existing in students:
        if existing.lower() == name:
            students.remove(existing)
            print(f"{existing} removed.")
            return
    print("Student not found.")


def search_student(students, keyword):
    keyword = keyword.strip().lower()
    # Partial match: "cruz" is found inside "Juan Cruz"
    found = [name for name in students if keyword in name.lower()]
    if len(found) == 0:
        print("No match found.")
    else:
        print(f"Found {len(found)}:")
        for name in sorted(found, key=str.lower):
            print(f"- {name}")


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
        print("2. Remove student")
        print("3. Search student")
        print("4. Display all students")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student(students, input("Enter student name: "))
        elif choice == "2":
            remove_student(students, input("Enter name to remove: "))
        elif choice == "3":
            search_student(students, input("Enter name to search: "))
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


main()

# List vs Set:
# A list keeps its items in order and allows duplicates, while a set has no order
# and does not allow duplicates. I used a list called students to store the names
# because I can sort it and number it when displaying. I used a list for the search
# results too. To block duplicates, I compare names in lowercase before adding,
# but a set could also do this job.