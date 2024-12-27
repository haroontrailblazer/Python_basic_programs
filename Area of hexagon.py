import math

# Function to calculate the area of a hexagon
def area_of_hexagon(x):
    # Calculate the area using the formula (3 * sqrt(3) * x^2) / 2
    area = (3 * math.sqrt(3) * x**2) / 2
    # Round the result to 1 decimal place
    return round(area, 1)

# Example usage:
print(area_of_hexagon(1))  # Expected output: 2.6
print(area_of_hexagon(2))  # Expected output: 10.4
print(area_of_hexagon(3))  # Expected output: 23.4