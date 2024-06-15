# Write a python program that calculates the sum of the digits of a given number.


def sum_of_digits(number):
    total_sum = 0
    
    for digit in str(number):
        total_sum += int(digit)
    
    return total_sum

number = int(input("Enter a number: "))

result = sum_of_digits(number)
print(f"The sum of the digits of {number} is {result}.")
