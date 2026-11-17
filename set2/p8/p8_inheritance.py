# Name: Mark Neilson Tol
# Section: IV-BSIT C
# Activity: P8 - Inheritance and Polymorphism
# Date: November 17, 2026


# Parent class: holds what every person has in common
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name}, {self.age} years old.")


# Child class 1: inherits from Person and adds its own attributes
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)   # reuse the parent's __init__
        self.student_id = student_id
        self.course = course

    # Override introduce() with a student-specific output
    def introduce(self):
        print(f"Hello! I am {self.name}, {self.age}, a {self.course} student "
              f"with ID {self.student_id}.")


# Child class 2: inherits from Person and adds its own attributes
class Teacher(Person):
    def __init__(self, name, age, subject, years_teaching):
        super().__init__(name, age)
        self.subject = subject
        self.years_teaching = years_teaching

    # Override introduce() with a teacher-specific output
    def introduce(self):
        print(f"Good day, class. I am {self.name}, and I have been teaching "
              f"{self.subject} for {self.years_teaching} years.")


# ---------- Demonstration ----------
print("=== P8: Inheritance and Polymorphism - Mark Neilson Tol ===\n")

# Objects of different classes in one list
people = [
    Person("Ana Reyes", 30),
    Student("Mark Neilson Tol", 21, "2022-001", "BSIT"),
    Student("Jim Cruz", 22, "2022-002", "BSIT"),
    Teacher("Carl Ferrer", 35, "Python and Node.js", 10),
]

# Polymorphism: same method call, different output depending on the object
for person in people:
    person.introduce()

# Extra: show the inheritance relationship
print()
for person in people:
    print(f"{person.name} is a {type(person).__name__} "
          f"(is a Person: {isinstance(person, Person)})")


# Explanation (replace with your own words before submitting):
# My program shows inheritance because Student and Teacher get name, age, and
# introduce() from the Person class, and each one calls super().__init__() to
# reuse the parent's setup. They also add their own attributes such as
# student_id and subject. It shows polymorphism because I put Person, Student,
# and Teacher objects in one list and call introduce() on each one in a loop.
# Python runs the overridden version for each object, so every one gives a
# different output.