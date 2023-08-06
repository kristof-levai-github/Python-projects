def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

try:
    numbers = []
    for i in range(10):
        num = int(input(f"Enter positive integer {i+1}: "))
        if num <= 0:
            print("Invalid input. Please enter a positive integer.")
            exit(1)
        numbers.append(num)

    smallest_prime = None
    for num in numbers:
        if is_prime(num):
            if smallest_prime is None or num < smallest_prime:
                smallest_prime = num

    if smallest_prime is not None:
        print(f"The smallest prime number is: {smallest_prime}")
    else:
        print("Not found.")
except ValueError:
    print("Invalid input. Please enter valid positive integers.")
