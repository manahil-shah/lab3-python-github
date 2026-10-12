
# simple Calculator

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b


def even_odd(number):
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")


def percentage(a, b):
    if b == 0:
        print("Error: Cannot calculate percentage with zero as the second number.")
        return None
    return (a / b) * 100


while True:
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Check Even or Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
        print("Calculator closed. Goodbye!")
        break

    elif choice in ("1", "2", "3", "4", "6"):
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if choice == "1":
            print("Result:", addition(a, b))

        elif choice == "2":
            print("Result:", subtraction(a, b))

        elif choice == "3":
            print("Result:", multiplication(a, b))

        elif choice == "4":
            result = division(a, b)
            if result is not None:
                print("Result:", result)

        elif choice == "6":
            result = percentage(a, b)
            if result is not None:
                print("Percentage:", result, "%")

    elif choice == "5":
        number = int(input("Enter an integer: "))
        even_odd(number)

    else:
        print("Invalid choice. Please select 1-7.")
