# Write a program in python that converts a string into a list of its characters


def string_to_list(string):
    return list(string)

user_input = input("Enter a string: ")
characters_list = string_to_list(user_input)
print("List of characters:", characters_list)
