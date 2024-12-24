import math

# Fixed values
C = 50
H = 30

# Function to calculate Q
def calculate_Q(D):
    return int(math.sqrt((2 * C * D) / H))

# Input comma-separated sequence of D values
input_sequence = input("Enter comma-separated values of D: ")
D_values = input_sequence.split(',')

# Calculate and print Q for each D value
result = [calculate_Q(int(D)) for D in D_values]
print(','.join(map(str, result)))