def read_real_number(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid real number.")

if __name__ == "__main__":
    lower_bound = read_real_number("Enter the lower bound of the interval: ", -1000, 1000)
    upper_bound = read_real_number("Enter the upper bound of the interval: ", -1000, 1000)

    if lower_bound >= upper_bound:
        print("Error: The lower bound must be less than the upper bound.")
    else:
        print(f"Interval: ({lower_bound}, {upper_bound})")
