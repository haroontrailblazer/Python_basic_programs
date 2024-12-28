def double_char(input_str):
    doubled_str = ""
    for char in input_str:
        doubled_str += char * 2
    return doubled_str

# Example usage
print(double_char("String"))        # Expected output: 'SSttrriinngg'
print(double_char("Hello World!"))  # Expected output: 'HHeelllloo  WWoorrlldd!!'
print(double_char("1234!_ "))       # Expected output: '11223344!!__  '