# Write a python program that generates the first n numbers in the Fibonacci sequence.


def fibonacci(n):

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

num = int(input("Enter the number of Fibonacci numbers to generate: "))

if num <= 0:
    print("Please enter a positive integer.")
else:
    fib_sequence = fibonacci(num)
    print(f"The first {num} numbers in the Fibonacci sequence are: {fib_sequence}")
