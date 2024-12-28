def index_of_caps(word):
    # Use list comprehension to find indices of capital letters
    return [i for i, char in enumerate(word) if char.isupper()]

# Test cases
print(index_of_caps("eDaBiT"))     # Expected output: [1, 3, 5]
print(index_of_caps("eQuINoX"))    # Expected output: [1, 3, 4, 6]
print(index_of_caps("determine"))  # Expected output: []
print(index_of_caps("STRIKE"))     # Expected output: [0, 1, 2, 3, 4, 5]
print(index_of_caps("sUn"))        # Expected output: [1]