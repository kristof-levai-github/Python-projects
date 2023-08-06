def search_char(arr, target):
    for i, char in enumerate(arr):
        if char == target:
            return i + 1
    return 0

def main():
    arr = "any character sequence"  # You can initialize the character array here
    target = input("Enter the character to search: ")

    result = search_char(arr, target)
    if result:
        print(f"Character '{target}' found at index {result}.")
    else:
        print(f"Character '{target}' not found in the array.")

if __name__ == "__main__":
    main()
