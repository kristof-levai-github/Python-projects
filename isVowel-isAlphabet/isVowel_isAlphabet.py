def is_alphabet_character(char):
    return char.isalpha()

def is_vowel(char):
    vowels = "AEIOUaeiou"
    return char in vowels

if __name__ == "__main__":
    user_input = input("Enter a character: ")

    if len(user_input) == 1 and is_alphabet_character(user_input):
        if is_vowel(user_input):
            print(f"{user_input} vowel")
        else:
            print(f"{user_input} consonant")
    else:
        print(f"{user_input} not in the English alphabet")
