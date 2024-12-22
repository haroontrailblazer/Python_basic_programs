def split_and_add(arr, k):
    if k <= 0 or k >= len(arr):
        return arr
    # Split the array into two parts
    first_part = arr[:k]
    second_part = arr[k:]
    # Add the first part to the end of the second part
    result = second_part + first_part
    return result

# Test the function
arr = [1, 2, 3, 4, 5]
k = 3
result = split_and_add(arr, k)
print("Original Array:", arr)
print("Array after splitting and adding:", result)