def uncommon_words(str1, str2):
    # Split the strings into words and convert them to sets
    words1 = set(str1.split())
    words2 = set(str2.split())
    # Find uncommon words by taking the set difference
    uncommon_words_set = words1.symmetric_difference(words2)
    # Convert the set of uncommon words back to a list
    uncommon_words_list = list(uncommon_words_set)
    return uncommon_words_list

# Input two strings
string1 = "This is the first string"
string2 = "This is the second string"

# Find uncommon words between the two strings
uncommon = uncommon_words(string1, string2)

# Print the uncommon words
print("Uncommon words:", uncommon)