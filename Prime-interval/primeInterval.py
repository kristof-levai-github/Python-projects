try:
    input_str = input("Enter two integer values separated by a comma: ")
    num1, num2 = map(int, input_str.split(','))

    if num1 > num2:
        num1, num2 = num2, num1  # Swap the values if num1 is greater than num2

    if num1 <= 1:
        num1 = 2

    prime_count = 0
    for num in range(num1, num2 + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_count += 1

    print(f"Number of prime numbers between {num1} and {num2}: {prime_count}")
except ValueError:
    print("Invalid input. Please enter two valid integer values separated by a comma.")
