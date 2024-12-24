import re

# Function to check if a password is valid
def is_valid_password(password):
    # Check the length of the password
    if 6 <= len(password) <= 12:
        # Check if the password matches all the criteria using regular expressions
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
            return True
    return False

# Initialize a list to store valid passwords
valid_passwords = []

# Accept input from the user as comma-separated passwords
passwords = input("Enter passwords separated by commas: ").split(',')

# Iterate through the passwords and check their validity
for psw in passwords:
    if is_valid_password(psw):
        valid_passwords.append(psw)

# Print the valid passwords separated by commas
print(','.join(valid_passwords))