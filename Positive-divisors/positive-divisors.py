try:
    number = int(input("Enter a positive number: "))
    if number <= 0:
        print("Invalid input. Please enter a positive number.")
    else:
        count = 0
        for i in range(1, number + 1):
            if number % i == 0:
                count += 1
        print(f"Number of positive divisors of {number}: {count}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
