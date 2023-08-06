try:
    N = int(input("Enter a positive integer: "))
    if N <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        count = 0
        for num in range(1, N + 1):
            if int(num**0.5)**2 == num:
                count += 1
        print(f"Number of perfect squares from 1 to {N}: {count}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
