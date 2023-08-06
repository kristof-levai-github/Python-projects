def swap_integers(a, b):
    return b, a

def main():
    try:
        input_str = input("Enter two integers separated by a comma: ")
        a, b = map(int, input_str.split(','))
        
        # Call the swap_integers function to swap the values
        a, b = swap_integers(a, b)
        
        print(f"Swapped values: {a}, {b}")
    except ValueError:
        print("Invalid input. Please enter two valid integers separated by a comma.")

if __name__ == "__main__":
    main()
