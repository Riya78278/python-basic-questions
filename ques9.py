# Write a python program that checks if a substring is present in a given string.


input1=input("enter the first string : ")
input2=input("enter the second string: ")
if input2 in input1:
    print(f"the substring <{input2}> is present in the main string --> {input1}")
else:
    print("No substring is present in the main string: ")    