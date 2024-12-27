def evenly_divisible(a, b, c):
    total = 0
    for num in range(a, b + 1):
        if num % c == 0:
            total += num
    return total

# Test cases
print(evenly_divisible(1, 10, 20))  # Expected output: 0 (no numbers between 1 and 10 are divisible by 20)
print(evenly_divisible(1, 10, 2))   # Expected output: 30 (2 + 4 + 6 + 8 + 10)
print(evenly_divisible(1, 10, 3))   # Expected output: 18 (3 + 6 + 9)