def read_integer(prompt, min_value, max_value):
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
    array = []
    for i in range(20):
        num = read_integer(f"Enter number {i + 1} (-1000 to 1000): ", -1000, 1000)
        array.append(num)

    positive_numbers = [num for num in array if num > 0]
    negative_numbers = [num for num in array if num < 0]

    average_positive = sum(positive_numbers) / len(positive_numbers) if positive_numbers else 0
    average_negative = sum(negative_numbers) / len(negative_numbers) if negative_numbers else 0

    print(f"\nPositive Numbers: {positive_numbers}")
    print(f"Negative Numbers: {negative_numbers}")

    print(f"\nAverage of Positive Numbers: {average_positive:.2f}")
    print(f"Average of Negative Numbers: {average_negative:.2f}")

    search_value = read_integer("Enter a number to search in the array: ", -1000, 1000)

    if search_value in array:
        position = array.index(search_value) + 1
        print(f"The searched value is the {position}th element of the array.")
    else:
        print("The searched value is not an element of the array.")
