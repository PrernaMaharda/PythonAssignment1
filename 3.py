n = int(input("Enter a number: "))
factorial = 1
if n == 0:
    print("The factorial of 0 is 1")
elif n < 0:
    print("The factorial of negative is 0")
else:
    for i in range(1, n+1):
        factorial = factorial * i
    print("The factorial of the given number is",factorial)

