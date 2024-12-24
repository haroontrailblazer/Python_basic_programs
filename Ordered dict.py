from collections import OrderedDict

# Create an OrderedDict
ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])

# Item to insert at the beginning
new_item = ('a', 1)

# Create a new OrderedDict with the new item as the first element
new_ordered_dict = OrderedDict([new_item])

# Merge the new OrderedDict with the original OrderedDict
new_ordered_dict.update(ordered_dict)

# Print the updated OrderedDict
print("Updated OrderedDict:", new_ordered_dict)