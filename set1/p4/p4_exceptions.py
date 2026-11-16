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

    

divide_numbers()