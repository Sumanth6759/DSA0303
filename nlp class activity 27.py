import re
from collections import Counter

# Step 1: Read a small text corpus
corpus = """
Natural language processing is a branch of artificial intelligence.
Natural language processing helps computers understand human language.
Language models predict the next word in a sentence.
"""

# Step 2: Tokenize the text into words
tokens = re.findall(r'\b[a-z]+\b', corpus.lower())

print("Tokens:")
print(tokens)

# Step 3: Generate unigram and bigram frequency counts

# Unigram frequencies
unigram_counts = Counter(tokens)

# Bigram frequencies
bigrams = []
for i in range(len(tokens) - 1):
    bigrams.append((tokens[i], tokens[i + 1]))

bigram_counts = Counter(bigrams)

print("\nUnigram Frequency Counts:")
for word, count in unigram_counts.items():
    print(f"{word}: {count}")

print("\nBigram Frequency Counts:")
for bg, count in bigram_counts.items():
    print(f"{bg}: {count}")

# Step 4: Compute unigram probabilities
total_words = len(tokens)

print("\nUnigram Probabilities:")
for word, count in unigram_counts.items():
    probability = count / total_words
    print(f"P({word}) = {probability:.4f}")

# Step 5: Compute bigram probabilities using MLE
print("\nBigram Probabilities (MLE):")
for (w1, w2), count in bigram_counts.items():
    probability = count / unigram_counts[w1]
    print(f"P({w2} | {w1}) = {probability:.4f}")

# Step 6 & 7: Check whether a given bigram exists
first = input("\nEnter first word of the bigram: ").lower()
second = input("Enter second word of the bigram: ").lower()

test_bigram = (first, second)

if test_bigram in bigram_counts:
    probability = bigram_counts[test_bigram] / unigram_counts[first]
    print("\nBigram exists in the corpus.")
    print(f"MLE Probability = {probability:.4f}")
else:
    print("\nBigram does not exist in the corpus.")
    print("Probability = 0")