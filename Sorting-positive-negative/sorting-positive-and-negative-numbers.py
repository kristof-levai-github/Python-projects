try:
    numbers = input("Enter a list of numbers separated by commas: ").split(',')
    numbers = [float(num) for num in numbers]

    positive_numbers = [num for num in numbers if num >= 0]
    negative_numbers = [num for num in numbers if num < 0]

    print("Positive numbers:", positive_numbers)
    print("Negative numbers:", negative_numbers)
except ValueError:
    print("Invalid input. Please enter valid numbers separated by commas.")
