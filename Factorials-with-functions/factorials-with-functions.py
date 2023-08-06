def calculate_factorial_int(N):
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
    return factorial

def calculate_factorial_long(N):
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
    return factorial

try:
    N = int(input("Enter a positive integer: "))
    if N <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        # Calculate factorial using int type variable
        factorial_int = calculate_factorial_int(N)
        print(f"The factorial of {N} (using int): {factorial_int}")

        # Calculate factorial using long type variable
        factorial_long = calculate_factorial_long(N)
        print(f"The factorial of {N} (using long): {factorial_long}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
