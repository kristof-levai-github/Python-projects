try:
    N = int(input("Enter a number: "))
    if N < 1:
        print("Invalid input. Please enter a positive integer.")
    else:
        total_sum = 0
        for num in range(1, N + 1):
            total_sum += num
        print(f"Sum of numbers from 1 to {N}: {total_sum}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
