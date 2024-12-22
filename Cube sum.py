def cube_sum_of_natural_numbers(n):
	if n <= 0:
		return 0
	else:
		total = sum([i**3 for i in range(1, n + 1)])
		return total

# Input the number of natural numbers
n = int(input("Enter the value of n: "))
if n <= 0:
	print("Please enter a positive integer.")
else:
	result = cube_sum_of_natural_numbers(n)
	print(f"The cube sum of the first {n} natural numbers is: {result}")