# Sample list containing lists
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]

# Using a list comprehension to remove empty lists
filtered_list = [i for i in list_of_lists if i]

# Print the filtered list
print("List after removing empty lists:", filtered_list)