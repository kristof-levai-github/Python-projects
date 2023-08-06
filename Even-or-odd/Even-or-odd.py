try:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("even")
    else:
        print("odd")
except ValueError:
    print("Invalid input. Please enter a valid number.")
