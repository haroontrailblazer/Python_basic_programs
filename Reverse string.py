# Function to reverse a string and swap the case of characters
def reverse(input_str):
    # Reverse the string and swap the case of characters
    reversed_str = input_str[::-1].swapcase()
    return reversed_str

# Test cases
print(reverse("Hello World"))  # Expected output: "DLROw OLLEh"
print(reverse("ReVeRsE"))      # Expected output: "eSrEvEr"
print(reverse("Radar"))        # Expected output: "RADAr"