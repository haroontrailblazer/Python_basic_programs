import math

# Function to convert radians to degrees
def radians_to_degrees(radians):
    # Convert radians to degrees using the formula degrees = radians * (180 / pi)
    degrees = radians * (180 / math.pi)
    # Round the result to 1 decimal place
    return round(degrees, 1)

# Test cases
print(radians_to_degrees(1))   # Expected output: 57.3
print(radians_to_degrees(20))  # Expected output: 1145.9
print(radians_to_degrees(50))  # Expected output: 2864.8