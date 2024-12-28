def num_layers(n):
    initial_thickness_mm = 0.5  # Initial thickness in millimeters
    final_thickness_mm = initial_thickness_mm * (2 ** n)
    final_thickness_m = final_thickness_mm / 1000  # Convert millimeters to meters
    return f"{final_thickness_m:.3f}m"

# Test cases
print(num_layers(1))  # Expected output: '0.001m'
print(num_layers(4))  # Expected output: '0.008m'
print(num_layers(21)) # Expected output: '1048.576m'