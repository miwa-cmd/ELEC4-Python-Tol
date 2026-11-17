# Name: Mark Neilson Tol
# Section: IV-BSIT C
# Activity: P6 - Recursion Toolkit
# Date: November 17, 2026


# Base case: n is 0 or 1, return 1
# Recursive call: n * factorial(n - 1)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Base case: n is 0 return 0, n is 1 return 1
# Recursive call: fibonacci(n - 1) + fibonacci(n - 2)
# Note: counting starts at 0, so fibonacci(0) = 0 and fibonacci(1) = 1
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: n is 0, return an empty list
# Recursive call: fibonacci_series(n - 1), then add the next term to the list
# This displays the first n terms without using a loop
def fibonacci_series(n):
    if n <= 0:
        return []
    return fibonacci_series(n - 1) + [fibonacci(n - 1)]


# Base case: n is 0, return 0
# Recursive call: n + sum_numbers(n - 1)
def sum_numbers(n):
    if n <= 0:
        return 0
    return n + sum_numbers(n - 1)


# Base case: the list is empty (return False) or the first item is the target (return True)
# Recursive call: search(items[1:], target), which checks the rest of the list
def search(items, target):
    if len(items) == 0:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def ask_number(prompt, max_value):
    """Ask for a whole number from 0 up to max_value. Ask again if invalid."""
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= max_value:
                return value
            print(f"Please enter a number from 0 to {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    while True:
        print("\n=== Recursion Toolkit - Mark Neilson Tol ===")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Sum of numbers from 1 to n")
        print("4. Search for a value in a list")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            n = ask_number("Enter n (0 to 500): ", 500)
            print(f"{n}! = {factorial(n)}")
        elif choice == "2":
            n = ask_number("Enter n (0 to 30): ", 30)
            print(f"The nth Fibonacci number (n = {n}): {fibonacci(n)}")
            print(f"First {n} terms: {fibonacci_series(n)}")
        elif choice == "3":
            n = ask_number("Enter n (0 to 900): ", 900)
            print(f"Sum of 1 to {n} = {sum_numbers(n)}")
        elif choice == "4":
            raw = input("Enter numbers separated by commas: ")
            try:
                items = [int(x.strip()) for x in raw.split(",")]
                target = int(input("Enter the number to search for: "))
                if search(items, target):
                    print(f"{target} is in the list.")
                else:
                    print(f"{target} is not in the list.")
            except ValueError:
                print("Invalid input. Please enter whole numbers only.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


main()