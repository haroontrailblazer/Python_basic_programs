# Write a function that stutters a word as if someone is struggling to read it. The first
#two letters are repeated twice with an ellipsis ... and space after each, and then the
#word is pronounced with a question mark ?.
def stutter(word):
    # Check if the word has at least two characters
    if len(word) < 2:
        return "Word must be at least two characters long."
    
    # Create the stuttered word by repeating the first two characters twice
    stuttered_word = f"{word[:2]}... {word[:2]}... {word}?"
    return stuttered_word

# Test cases
print(stutter("incredible"))  # Expected: "in... in... incredible?"
print(stutter("enthusiastic"))  # Expected: "en... en... enthusiastic?"
print(stutter("outstanding"))  # Expected: "ou... ou... outstanding?"