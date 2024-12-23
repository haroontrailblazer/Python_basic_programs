# Sample list of numbers
numbers = [30, 10, -45, 5, 20]

# Initialize a variable to store the minimum value, initially set to the first element
minimum = numbers[0]

# Iterate through the list and update the minimum value if a smaller number is found
for i in numbers:
    if i < minimum:
        minimum = i

# Print the minimum value
print("The smallest number in the list is:", minimum)