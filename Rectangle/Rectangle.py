def read_positive_real_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid positive real number.")

if __name__ == "__main__":
    length = read_positive_real_number("Enter the length of the rectangle: ")
    width = read_positive_real_number("Enter the width of the rectangle: ")

    perimeter = 2 * (length + width)
    area = length * width

    print(f"The perimeter of the rectangle is: {perimeter:.2f}")
    print(f"The area of the rectangle is: {area:.2f}")
