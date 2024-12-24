# Accept input from the user
input_sequence = input("Enter a comma-separated sequence of words: ")

# Split the input into a list of words
words = input_sequence.split(',')

# Remove any leading/trailing whitespace from each word
words = [word.strip() for word in words]

# Sort the words alphabetically
sorted_words = sorted(words)

# Join the sorted words into a comma-separated sequence
sorted_sequence = ','.join(sorted_words)

# Print the sorted sequence
print("Sorted words:", sorted_sequence)