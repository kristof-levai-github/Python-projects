try:
    N = int(input("Enter a positive integer: "))
    if N <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        # Using int type variable for factorial
        factorial_int = 1
        for i in range(1, N + 1):
            factorial_int *= i
        print(f"The factorial of {N} (using int): {factorial_int}")

        # Using long type variable for factorial
        factorial_long = 1
        for i in range(1, N + 1):
            factorial_long *= i
        print(f"The factorial of {N} (using long): {factorial_long}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
