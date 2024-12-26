subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]
sentences = []

for sub in subjects:
    for vrb in verbs:
        for obj in objects:
            sentence = f"{sub} {vrb} {obj}."
            sentences.append(sentence)

for sentence in sentences:
    print(sentence)