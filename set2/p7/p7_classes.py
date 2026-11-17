# Name: Mark Neilson Tol
# Section: IV-BSIT C
# Activity: P7 - Student Management System with Classes
# Date: November 17, 2026


class Subject:
    """A subject with a code, a title, and a number of units."""

    def __init__(self, code, title, units):
        self.code = code
        self.title = title
        self.units = units

    def display(self):
        print(f"  {self.code} - {self.title} ({self.units} units)")


class Student:
    """A student whose grade is private (__grade) and can only be
    read or changed through methods."""

    def __init__(self, student_id, name, course, grade):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.__grade = 0          # private attribute, set below
        self.set_grade(grade)     # reuse validation in the constructor

    # Getter: read the private grade
    def get_grade(self):
        return self.__grade

    # Setter: change the private grade, but reject invalid values
    def set_grade(self, new_grade):
        if not isinstance(new_grade, (int, float)) or isinstance(new_grade, bool):
            raise ValueError("Grade must be a number.")
        if new_grade < 0 or new_grade > 100:
            raise ValueError("Grade must be from 0 to 100.")
        self.__grade = new_grade

    # Update the student's information (only the values that are given)
    def update_info(self, name=None, course=None):
        if name:
            self.name = name
        if course:
            self.course = course

    def display(self):
        status = "Passed" if self.__grade >= 75 else "Failed"
        print(f"  [{self.student_id}] {self.name} | {self.course} | "
              f"Grade: {self.__grade} ({status})")


class Section:
    """A section that holds many Student objects and many Subject objects."""

    def __init__(self, name, adviser):
        self.name = name
        self.adviser = adviser
        self.students = []    # list of Student objects
        self.subjects = []    # list of Subject objects

    def add_student(self, student):
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def list_students(self):
        print(f"\nSection {self.name} (Adviser: {self.adviser})")
        print(f"Students ({len(self.students)}):")
        for student in self.students:
            student.display()

    def list_subjects(self):
        print(f"\nSubjects of {self.name}:")
        for subject in self.subjects:
            subject.display()


# ---------- Demonstration ----------
print("=== P7: School System - Mark Neilson Tol ===")

# Create the section and its subjects
section = Section("IV-BSIT C", "Mr. Carl Ferrer")
section.add_subject(Subject("ELEC 3", "Node.js", 3))
section.add_subject(Subject("ELEC 4", "Python Programming", 3))

# Create three (or more) student objects
s1 = Student("2022-001", "Mark Neilson Tol", "BSIT", 90)
s2 = Student("2022-002", "Jim Cruz", "BSIT", 82.5)
s3 = Student("2022-003", "Jit Lee Santos", "BSIT", 70)

# Add the students to the section
section.add_student(s1)
section.add_student(s2)
section.add_student(s3)

section.list_subjects()
section.list_students()

# Update one student (info and private grade)
print("\n--- Updating Jit Lee Santos ---")
s3.update_info(name="Jit Lee M. Santos", course="BSIT-IV")
s3.set_grade(88)
print(f"New grade read through get_grade(): {s3.get_grade()}")

# Try an invalid grade: the setter must reject it
print("\n--- Trying to set an invalid grade (150) on Jim Cruz ---")
try:
    s2.set_grade(150)
except ValueError as error:
    print(f"Rejected: {error}")
print(f"Jim's grade is still {s2.get_grade()}")

# Display all students again after the update
section.list_students()


# Notes (for the video):
# - __grade is private. Python renames it to _Student__grade, so writing
#   s1.__grade = 200 from outside does not change the real grade.
# - Section "has" Students and Subject (composition): the classes work together.