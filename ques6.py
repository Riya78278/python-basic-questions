# Write a program that reads the content of a text file and prints it to the console.


filename="ques6.txt"
try:
    with open(filename,"r") as file:
        content=file.read()
    print("the content which is written in the file is : ")
    print(content)    
except FileNotFoundError:
    print(f"the file {filename} doesnt exist...")
      
    
