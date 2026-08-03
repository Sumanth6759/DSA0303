import random

# Probabilistic dictionary
prob_tags = {
    "I": ["PRP"],
    "eat": ["VB", "NN"],
    "apple": ["NN"],
    "can": ["MD", "NN"],
    "play": ["VB", "NN"]
}

sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nAssigned POS Tags")

for word in words:
    if word in prob_tags:
        tag = random.choice(prob_tags[word])
    else:
        tag = "NN"

    print(word, "->", tag)