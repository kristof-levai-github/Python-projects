import math

def read_positive_real_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid real number.")

if __name__ == "__main__":
    radius = read_positive_real_number("Enter the radius of the circle: ")

    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    print(f"The area of the circle with radius {radius} is: {area:.2f}")
    print(f"The circumference of the circle with radius {radius} is: {circumference:.2f}")
