def perform_operation(op, num1, num2):
    if op == '1':
        return num1 + num2
    elif op == '2':
        return num1 - num2
    elif op == '3':
        return num1 * num2
    elif op == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation selected."

def math_calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input for operation
    operation = input("Enter the number of the operation you want to perform: ")

    # Get user input for numbers
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Perform the selected operation
    result = perform_operation(operation, number1, number2)
    print(f"The result is: {result}")

math_calculator()
