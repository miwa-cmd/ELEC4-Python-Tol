# Name: Mark Neilson Tol
# Section: IV-BSIT C
# Activity: P4 - Safe Menu Program
# Date: November 16, 2026


def divide_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a / b
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Result:", result)
    finally:
        print("Division attempt finished.")


def open_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as file:
            print("\n--- File contents ---")
            print(file.read())
    except FileNotFoundError:
        print("File not found. Please check the file name.")


def main():
    while True:
        print("\n=== Safe Menu Program - Mark Neilson Tol ===")
        print("1. Divide two numbers")
        print("2. Open a file")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()