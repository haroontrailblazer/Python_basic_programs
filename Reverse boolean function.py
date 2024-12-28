def reverse(value):
    if isinstance(value, bool):
        return not value
    else:
        return "boolean expected"

# Example usage
print(reverse(True))   # Expected output: False
print(reverse(False))  # Expected output: True
print(reverse(1))      # Expected output: "boolean expected"
print(reverse("True")) # Expected output: "boolean expected"