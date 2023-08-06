import math

def calculate_arithmetic_mean(x, y):
    return (x + y) / 2

def calculate_geometric_mean(x, y):
    return math.sqrt(x * y)

if __name__ == "__main__":
    try:
        x = float(input("Enter the first positive number: "))
        y = float(input("Enter the second positive number: "))

        if x <= 0 or y <= 0:
            print("Both numbers should be positive.")
        else:
            arithmetic_mean = calculate_arithmetic_mean(x, y)
            geometric_mean = calculate_geometric_mean(x, y)

            print("Arithmetic Mean: ", arithmetic_mean)
            print("Geometric Mean: ", geometric_mean)
    except ValueError:
        print("Invalid input. Please enter valid real numbers.")
