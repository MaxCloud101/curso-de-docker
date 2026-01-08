import sys

def factorial(n):
    # Base case: when n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

if len(sys.argv) > 1:
    number = int(sys.argv[1])
    print(factorial(number))
else:
    print("No arguments")
