#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.


lines = []
print("Enter multiple lines of text. Press Enter on an empty line to stop:")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("You entered the following lines:")
for line in lines:
    print(line)
