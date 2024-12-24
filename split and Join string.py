# Split a string into a list of words
input_str = "Python program to split and join a string"
word_list = input_str.split()  # By default, split on whitespace

# Join the list of words into a string
separator = " "  # specify the separator between words
output_str = separator.join(word_list)

# Print the results
print("Original String:", input_str)
print("List of split Words:", word_list)
print("Joined String:", output_str)