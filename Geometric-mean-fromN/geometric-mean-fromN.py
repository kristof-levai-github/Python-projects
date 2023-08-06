import math

try:
    N = int(input("Enter a number: "))
    if N < 1:
        print("Invalid input. Please enter a positive integer.")
    else:
        product = 1
        for i in range(1, N + 1):
            product *= i

        geometric_mean = pow(product, 1.0 / N)
        print(f"Geometric mean: {geometric_mean}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
