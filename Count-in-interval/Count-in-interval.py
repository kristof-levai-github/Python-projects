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
    lower_bound = read_real_number("Enter the lower bound of the interval: ")
    upper_bound = read_real_number("Enter the upper bound of the interval: ")

    if lower_bound >= upper_bound:
        print("Error: The lower bound must be less than the upper bound.")
    else:
        n = read_integer("Enter the number of elements: ")
        numbers_within_interval = 0

        for i in range(n):
            num = read_real_number(f"Enter number {i + 1}: ")
            if lower_bound <= num <= upper_bound:
                numbers_within_interval += 1

        print(f"\nNumber of elements within the interval: {numbers_within_interval}")
