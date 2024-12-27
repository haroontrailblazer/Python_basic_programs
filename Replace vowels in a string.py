def replace_vowels(string, char):
    vowels = "AEIOUaeiou"  # List of vowels to be replaced
    for vowel in vowels:
        string = string.replace(vowel, char)  # Replace each vowel with the specified character
    return string

# Test cases
print(replace_vowels("the aardvark", "#"))  # Expected output: "th# ##rdv#rk"
print(replace_vowels("minnie mouse", "?"))  # Expected output: "m?nn?? m??s?"
print(replace_vowels("shakespeare", "*"))   # Expected output: "sh*k*sp**r*"