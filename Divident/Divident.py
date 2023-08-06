import math

def read_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def read_real_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid real number.")

if __name__ == "__main__":
    print("Enter two integerss:")
    dividend = read_integer("Dividend: ")
    divisor = read_integer("Divisor: ")

    if divisor != 0:
        quotient = dividend // divisor
        remainder = dividend % divisor
        print(f"{dividend} / {divisor} = {quotient}, remainder: {remainder}")
    else:
        print("Error: Division by zero is not allowed.")

    print("\nEnter two real numbers:")
    real_dividend = read_real_number("Dividend: ")
    real_divisor = read_real_number("Divisor: ")

    if real_divisor != 0.0:
        real_quotient = real_dividend / real_divisor
        real_remainder = math.fmod(real_dividend, real_divisor)
        print(f"{real_dividend:.2f} / {real_divisor:.2f} = {real_quotient:.2f}, remainder: {real_remainder:.2f}")
    else:
        print("Error: Division by zero is not allowed.")
1