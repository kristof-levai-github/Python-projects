def is_perfect_number(number):
    divisors_sum = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i
    return divisors_sum == number

def count_perfect_numbers(N):
    if not isinstance(N, int) or N <= 1:
        return "Invalid input"

    count = 0
    for num in range(1, N + 1):
        if is_perfect_number(num):
            count += 1

    return count

def main():
    try:
        N = int(input("Enter a positive integer greater than 1: "))
        perfect_count = count_perfect_numbers(N)
        print(f"Number of perfect numbers from 1 to {N}: {perfect_count}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
