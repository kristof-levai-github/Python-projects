def is_palindrome(text):
    
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())


    return cleaned_text == cleaned_text[::-1]

def main():
    try:
        text = input("Enter a text: ")
        if is_palindrome(text):
            print("The text is a palindrome.")
        else:
            print("The text is not a palindrome.")
    except ValueError:
        print("Invalid input. Please enter a valid text.")

if __name__ == "__main__":
    main()
