def is_disarium(num):
    num_str = str(num)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    return num == digit_sum

disarium_numbers = [num for num in range(1, 101) if is_disarium(num)]
print("Disarium numbers between 1 and 100:")
for num in disarium_numbers:
    print(num, end=" | ")