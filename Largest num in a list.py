# Sample list of numbers
numbers = [30, 10, -45, 5, 20]

# Initialize a variable to store the maximum value, initially set to the first element
maximum = numbers[0]

# Iterate through the list and update the maximum value if a larger number is found
for i in numbers:
    if i > maximum:
        maximum = i

# Print the maximum value
print("The largest number in the list is:", maximum)