# Sample dictionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}

# Initialize an empty set to store unique values
uni_val = set()

# Iterate through the values of the dictionary
for i in my_dict.values():
    # Add each value to the set
    uni_val.add(i)

# Convert the set of unique values back to a list (if needed)
unique_values_list = list(uni_val)

# Print the unique values
print("Unique values in the dictionary:", unique_values_list)