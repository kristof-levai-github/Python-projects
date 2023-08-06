def read_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_square(num):
    return num * num

if __name__ == "__main__":
    try:
        number = read_integer("Enter an integer: ")
        square = calculate_square(number)
        print(f"The square of {number} is: {square}")
    except ValueError:
        print("Invalid input.")
