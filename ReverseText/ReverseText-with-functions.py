def reverse_text_in_place(text):
    # Convert the text to a character array (list)
    char_array = list(text)
    
    left = 0
    right = len(char_array) - 1
    
    while left < right:
        char_array[left], char_array[right] = char_array[right], char_array[left]
        left += 1
        right -= 1
    

    reversed_text = "".join(char_array)
    
    return reversed_text

def main():
    # Initialize the character array with any text that may contain spaces
    text = "Hello, World! This is a test text."
    
    reversed_text = reverse_text_in_place(text)
    
    print("Original text:", text)
    print("Reversed text:", reversed_text)

if __name__ == "__main__":
    main()
