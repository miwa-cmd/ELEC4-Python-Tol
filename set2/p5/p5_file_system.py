# Name: Mark Neilson Tol
# Section: IV-BSIT C
# Activity: P5 - Student Information File System
# Date: November 17, 2026

import os

# students.txt is saved in the same folder as this program,
# so it works no matter where the program is run from
FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.txt")


def load_students():
    """Load all records from the file. If the file does not exist, return an empty list."""
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                try:
                    # Each line: ID|Full Name|Course/Section|Average
                    students.append({
                        "id": parts[0],
                        "name": parts[1],
                        "course": parts[2],
                        "average": float(parts[3]),
                    })
                except (IndexError, ValueError):
                    print(f"Skipped a bad line in the file: {line}")
    except FileNotFoundError:
        print("students.txt not found yet. Starting with an empty list.")
    return students


def save_students(students):
    """Write all records to the file, one student per line."""
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(f"{s['id']}|{s['name']}|{s['course']}|{s['average']}\n")


def clean(text):
    """Remove the separator character so it cannot break the file format."""
    return text.replace("|", "-").strip()


def ask_average(prompt):
    """Keep asking until the user enters a number from 0 to 100."""
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            print("Average must be from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def find_student(students, student_id):
    """Return the student with the given ID, or None."""
    for s in students:
        if s["id"].lower() == student_id.lower():
            return s
    return None


def add_student(students):
    student_id = clean(input("Student ID: "))
    if not student_id:
        print("ID cannot be empty.")
        return
    if find_student(students, student_id):
        print("That ID already exists.")
        return
    name = clean(input("Full name: "))
    course = clean(input("Course/Section: "))
    if not name or not course:
        print("Name and course/section cannot be empty.")
        return
    average = ask_average("General average (0-100): ")
    students.append({"id": student_id, "name": name, "course": course, "average": average})
    save_students(students)
    print("Student added and saved.")


def display_students(students):
    if not students:
        print("No records yet.")
        return
    print(f"\n{'ID':<12}{'Name':<25}{'Course/Section':<18}{'Average':<8}")
    print("-" * 63)
    for s in students:
        print(f"{s['id']:<12}{s['name']:<25}{s['course']:<18}{s['average']:<8}")


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()
    s = find_student(students, student_id)
    if s:
        print(f"Found: {s['id']} | {s['name']} | {s['course']} | {s['average']}")
    else:
        print("Student not found.")


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()
    s = find_student(students, student_id)
    if not s:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    new_name = clean(input(f"Full name [{s['name']}]: "))
    new_course = clean(input(f"Course/Section [{s['course']}]: "))
    new_average = input(f"General average [{s['average']}]: ").strip()

    if new_name:
        s["name"] = new_name
    if new_course:
        s["course"] = new_course
    if new_average:
        try:
            value = float(new_average)
            if 0 <= value <= 100:
                s["average"] = value
            else:
                print("Average must be from 0 to 100. Average not changed.")
        except ValueError:
            print("Invalid average. Average not changed.")
    save_students(students)
    print("Record updated and saved.")


def main():
    students = load_students()
    while True:
        print("\n=== Student Information File System - Mark Neilson Tol ===")
        print("1. Add student")
        print("2. Display all students")
        print("3. Search by ID")
        print("4. Update student")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


main()