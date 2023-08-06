def read_integer_in_range(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    lower_bound = read_integer_in_range("Enter the lower bound of the interval (min: 50, max: 100): ", 50, 100)
    upper_bound = read_integer_in_range("Enter the upper bound of the interval (min: 50, max: 100): ", 50, 100)

    if lower_bound >= upper_bound:
        print("Error: The lower bound must be less than the upper bound.")
    else:
        print(f"Interval: ({lower_bound}, {upper_bound})")
