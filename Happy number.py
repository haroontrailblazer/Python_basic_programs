def is_happy_number(num):
    seen = set()  # To store previously seen numbers
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))
    return num == 1

# Test the function with a number
num = int(input("Enter a number: "))
if is_happy_number(num):
    print(f"{num} is a Happy Number")
else:
    print(f"{num} is not a Happy Number")