# Write a python program that calculates the factorial of a given number.


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
a=int(input("enter the number : "))
if(a<0):
    print("give the valid number between 0 to infinity")
else:
    result=factorial(a)
    print("the factorial of the given number is ",result)    