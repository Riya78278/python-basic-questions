# Write a python program that takes a list of numbers and returns their sum.


def sum_of_numbers(numbers):
    total_sum = 0
    
    for number in numbers:
        total_sum += number
    
    return total_sum

numbers_input = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers_input.split()]
result = sum_of_numbers(numbers_list)
print(f"The sum of the numbers is: {result}")
