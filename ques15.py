# Write a program that reads data from a CSV file and prints it to the console.


import csv

filename="ques15.csv"
try:
    with open(filename,"r") as file:
        csv_reader= csv.reader(file)

        for row in csv_reader:
            print (row)

except FileNotFoundError:
    print(f"the file{filename} doesnt exist ..")