def factorial(n):
    """factorial of a number """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

x = int(input("Enter a number to calculate factorial: "))
help(factorial)
print(factorial(x))