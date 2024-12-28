def filter_list(lst):
    # Initialize an empty list to store non-string elements
    result = []
    # Iterate through the elements in the input list
    for element in lst:
        # Check if the element is a non-negative integer (not a string)
        if isinstance(element, int) and element >= 0:
            result.append(element)
    return result

# Test cases
print(filter_list([1, 2, "a", "b"]))  # Expected output: [1, 2]
print(filter_list([1, "a", "b", 0, 15]))  # Expected output: [1, 0, 15]
print(filter_list([1, 2, "aasf", "1", "123", 123]))  # Expected output: [1, 2, 123]