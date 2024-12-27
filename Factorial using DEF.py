def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

# Test cases
print(factorial(5))  # Expected output: 120
print(factorial(3))  # Expected output: 6
print(factorial(1))  # Expected output: 1
print(factorial(0))  # Expected output: 1