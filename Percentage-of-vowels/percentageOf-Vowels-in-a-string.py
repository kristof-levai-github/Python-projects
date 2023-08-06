def calculate_percentage_vowels(text):
    vowels = "AEIOUaeiou"
    vowel_count = sum(1 for char in text if char in vowels)
    total_chars = len(text)
    percentage_vowels = (vowel_count / total_chars) * 100
    return percentage_vowels

if __name__ == "__main__":
    user_input = input("Enter a character string: ")

    percentage_of_vowels = calculate_percentage_vowels(user_input)

    print(f"Percentage of vowels: {percentage_of_vowels:.2f}%")
