# Sample dictionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40,
    'e': 50
}

# Initialize a variable to store the sum
total_sum = 0

# Iterate through the values of the dictionary and add them to the total
for i in my_dict.values():
    total_sum += i

# Print the sum of all items in the dictionary
print("Sum of all items in the dictionary:", total_sum)