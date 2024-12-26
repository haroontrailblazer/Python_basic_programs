def fibonacci(n):
    sequence = [0, 1]  # Initializing the sequence with the first two Fibonacci numbers
    [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, n)]
    return sequence

try:
    n = int(input("Enter a value for n: "))
    result = fibonacci(n)
    print(','.join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")