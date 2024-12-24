def remove_char(input_str, i):
    # Check if i is a valid index
    if i < 0 or i >= len(input_str):
        print(f"Invalid index {i}. The string remains unchanged.")
        return input_str
    # Remove the i-th character using slicing
    result_str = input_str[:i] + input_str[i + 1:]
    return result_str

# Input string
input_str = "Hello, wWorld!"
i = 7  # Index of the character to remove

# Remove the i-th character
new_str = remove_char(input_str, i)
print(f"Original String: {input_str}")
print(f"String after removing {i}th character: {new_str}")