def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_twin_prime_pairs(N):
    if not isinstance(N, int) or N <= 1:
        return "Invalid input"

    twin_prime_count = 0
    for i in range(2, N - 1):
        if is_prime(i) and is_prime(i + 2):
            twin_prime_count += 1

    return twin_prime_count

def main():
    try:
        N = int(input("Enter a positive integer greater than 1: "))
        twin_prime_count = count_twin_prime_pairs(N)
        print(f"Number of twin prime pairs from 1 to {N}: {twin_prime_count}")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
