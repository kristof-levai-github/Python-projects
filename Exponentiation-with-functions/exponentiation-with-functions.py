def perform_exponentiation(base, exponent):
    return base ** exponent

try:
    input_str = input("Enter two non-negative numbers separated by a comma: ")
    base, exponent = map(float, input_str.split(','))

    if base < 0 or exponent < 0:
        print("Invalid input. Please enter non-negative numbers.")
    else:
        result = perform_exponentiation(base, exponent)
        print(f"The result of {base} raised to the power of {exponent}: {result}")
except ValueError:
    print("Invalid input. Please enter valid non-negative numbers separated by a comma.")
