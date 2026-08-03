import re

sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nRule-Based POS Tags")

for word in words:

    if re.fullmatch(r".*ing", word):
        tag = "VBG"

    elif re.fullmatch(r".*ed", word):
        tag = "VBD"

    elif re.fullmatch(r".*ly", word):
        tag = "RB"

    elif re.fullmatch(r".*s", word):
        tag = "NNS"

    else:
        tag = "NN"

    print(word, "->", tag)