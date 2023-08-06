def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False

    return True

if __name__ == "__main__":
    user_input = int(input("Enter an integer: "))

    if is_prime(user_input):
        print(f"{user_input} is prime.")
    else:
        print(f"{user_input} is not prime.")
