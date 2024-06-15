# Write a program in python that counts the frequency of each character in a string.


def count_characters(string):
    char_frequency = {}

    for char in string:
        # Increment the count of the character in the dictionary
        char_frequency[char] = char_frequency.get(char, 0) + 1

    return char_frequency

user_input = input("Enter a string: ")

frequency_dict = count_characters(user_input)

print("Frequency of each character:")
for char, freq in frequency_dict.items():
    print(f"'{char}': {freq}")
