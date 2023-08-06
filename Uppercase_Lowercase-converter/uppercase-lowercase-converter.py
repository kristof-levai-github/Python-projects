def read_text():
    text = input("Enter any text (may contain spaces): ")
    return text

def convert_to_lowercase(text):
    return text.lower()

def convert_to_uppercase(text):
    return text.upper()

if __name__ == "__main__":
    text = read_text()

    result_lowercase = convert_to_lowercase(text)
    result_uppercase = convert_to_uppercase(text)

    print(f"Original Text: {text}")
    print(f"Text in lowercase: {result_lowercase}")
    print(f"Text in uppercase: {result_uppercase}")
