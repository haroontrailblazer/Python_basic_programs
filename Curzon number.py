def is_curzon(num):
    # Calculate the numerator (2^num + 1)
    numerator = 2 ** num + 1
    # Calculate the denominator (2 * num + 1)
    denominator = 2 * num + 1
    # Check if the numerator is divisible by the denominator
    return numerator % denominator == 0

# Test cases
print(is_curzon(5))  # Expected output: True
print(is_curzon(10)) # Expected output: False
print(is_curzon(14)) # Expected output: True