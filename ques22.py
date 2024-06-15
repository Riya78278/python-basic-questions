# Write a python program that returns the minimum and maximum values in a list of numbers.


def find_min_max(numbers):
    if not numbers:
        return None, None
    
    minimum = min(numbers)
    maximum = max(numbers)
    
    return minimum, maximum

numbers_list = [5, 3, 8, 2, 9, 1, 6]
minimum_value, maximum_value = find_min_max(numbers_list)
print(f"The minimum value in the list is: {minimum_value}")
print(f"The maximum value in the list is: {maximum_value}")
