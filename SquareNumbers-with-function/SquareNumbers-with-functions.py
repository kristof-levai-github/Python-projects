def count_square_numbers(N):
    if not isinstance(N, int) or N < 0:
        return "Invalid input"

    count = 0
    for i in range(N + 1):
        if i ** 0.5 == int(i ** 0.5):
            count += 1

    return count

def main():
    try:
        N = int(input("Enter a positive integer: "))
        square_count = count_square_numbers(N)
        print(f"Number of square numbers from 0 to {N}: {square_count}")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
