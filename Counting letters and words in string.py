# Accept input from the user
sentence = input("Enter a sentence: ")

# Initialize counters for letters and digits
letter_count = 0
digit_count = 0

# Iterate through each character in the sentence
for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

# Print the results
print("LETTERS", letter_count)
print("DIGITS", digit_count)