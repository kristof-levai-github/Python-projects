def perform_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Error: Division by zero is not allowed.")
    elif operation == '%':
        if num2 != 0:
            return num1 % num2
        else:
            raise ValueError("Error: Division by zero is not allowed.")
    else:
        raise ValueError("Invalid operation.")

if __name__ == "__main__":
    try:
        operation_input = input("Enter the operation (e.g., 5+2): ")
        num1, operation, num2 = operation_input.split()
        num1 = float(num1)
        num2 = float(num2)

        result = perform_operation(num1, num2, operation)
        print(f"{result:.2f}")

    except ValueError as e:
        print(e)
