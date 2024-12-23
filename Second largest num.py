# Sample list of numbers
numbers = [30, 10, 45, 5, 20]

# Sort the list in descending order
numbers.sort(reverse=True)

# Check if there are at least two elements in the list
if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number.")