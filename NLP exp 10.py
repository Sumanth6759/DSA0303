# Initial dictionary

dictionary = {
    "I": "PRP",
    "can": "NN",
    "fish": "NN",
    "swim": "VB"
}

sentence = input("Enter a sentence: ")

words = sentence.split()

tags = []

# Initial tagging
for word in words:
    tags.append(dictionary.get(word, "NN"))

# Transformation Rule:
# If previous word is PRP and current word is "can",
# change tag from NN to MD.

for i in range(1, len(words)):
    if words[i] == "can" and tags[i-1] == "PRP":
        tags[i] = "MD"

print("\nTransformation-Based POS Tags")

for word, tag in zip(words, tags):
    print(word, "->", tag)