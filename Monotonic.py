def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing

# Test the function
arr1 = [1, 2, 2, 3]  # Monotonic (non-decreasing)
arr2 = [3, 2, 1]     # Monotonic (non-increasing)
arr3 = [1, 3, 2, 4]  # Not monotonic

print("arr1 is monotonic:", is_monotonic(arr1))
print("arr2 is monotonic:", is_monotonic(arr2))
print("arr3 is monotonic:", is_monotonic(arr3))