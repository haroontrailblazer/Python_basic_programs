def correct_signs(expression):
    try:
        return eval(expression)
    except:
        return False

# Test cases
print(correct_signs("3 < 7 < 11"))  # Expected output: True
print(correct_signs("13 > 44 > 33 < 1"))  # Expected output: False
print(correct_signs("1 < 2 < 6 < 9 > 3"))  # Expected output: True