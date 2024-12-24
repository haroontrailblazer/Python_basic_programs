# Sort by Keys
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_keys = dict(sorted(sample_dict.items()))

print("Sorted by keys:")
for key, value in sorted_dict_by_keys.items():
    print(f"{key}: {value}")