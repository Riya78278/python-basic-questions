# Write a program that takes a string input from the user and writes it to a text file.


user_input=input("enter a string: ")
filename="ques5.txt"

with open(filename,"w") as file:
    file.write(user_input)

print(f"the input has been written to {filename}.")    