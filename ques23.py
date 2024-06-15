# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

conversion_type = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ")
if conversion_type.upper() == 'C':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")
elif conversion_type.upper() == 'F':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"The temperature in Celsius is: {celsius:.2f}°C")
else:
    print("Invalid input. Please enter 'C' or 'F'.")

