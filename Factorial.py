def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number to compute its factorial: "))
print(f"The factorial of {num} is {factorial(num)}")
