import random

text = "I love natural language processing and I love Python programming"

words = text.split()

# Build Bigram Model
bigram = {}

for i in range(len(words)-1):
    word = words[i]
    next_word = words[i+1]

    if word not in bigram:
        bigram[word] = []

    bigram[word].append(next_word)

# Generate Text
current = random.choice(words)
generated = [current]

for i in range(10):
    if current in bigram:
        current = random.choice(bigram[current])
        generated.append(current)
    else:
        break

print("Generated Text:")
print(" ".join(generated))