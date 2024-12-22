def is_disarium(number):
    # Convert the number to a string to iterate over its digits
    num_str = str(number)
    # Calculate the sum of digits raised to their respective positions
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    # Check if the sum is equal to the original number
    return digit_sum == number

# Input a number from the user
try:
    num = int(input("Enter a number: "))
    # Check if it's a Disarium number
    if is_disarium(num):
        print(f"{num} is a Disarium number.")
    else:
        print(f"{num} is not a Disarium number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")