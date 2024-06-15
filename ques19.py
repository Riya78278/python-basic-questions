# Write a python program that removes all punctuation from a given string.


import string

def remove_punctuation(input_string):
   
    translation_table = str.maketrans("", "", string.punctuation)
    
    cleaned_string = input_string.translate(translation_table)
    return cleaned_string

user_input = input("Enter a string: ")

cleaned_string = remove_punctuation(user_input)
print(f"The string without punctuation is: {cleaned_string}")
