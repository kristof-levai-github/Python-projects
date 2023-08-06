def read_real_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid real number.")

if __name__ == "__main__":
    number = read_real_number("Enter a real number: ")

    absolute_value = abs(number)

    print(f"The absolute value of {number} is: {absolute_value:.2f}")
