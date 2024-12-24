from collections import OrderedDict

def check_order(string, reference):
    # Create OrderedDicts for both strings
    string_dict = OrderedDict.fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)
    # Check if the OrderedDict for the string matches the OrderedDict for the reference
    return string_dict == reference_dict

# Input strings
input_string = "hello world"
reference_string = "helo wrd"

# Check if the order of characters in input_string matches reference_string
if check_order(input_string, reference_string):
    print("The order of characters in the input string matches the reference string.")
else:
    print("The order of characters in the input string does not match the reference string.")