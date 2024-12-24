def find_duplicates(input_str):
    # Create an empty dictionary to store character counts
    char_count = {}
    # Initialize a list to store duplicate characters
    duplicates = []
    # Iterate through each character in the input string
    for i in input_str:
        # If the character is already in the dictionary, increment its count
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    # Iterate through the dictionary and add characters with count > 1
    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)
    return duplicates

# Input a string
input_string = "piyush sharma"
# Find duplicate characters in the string
duplicate_chars = find_duplicates(input_string)
# Print the list of duplicate characters
print("Duplicate characters:", duplicate_chars)