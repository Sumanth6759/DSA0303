# Import required libraries
import nltk
from nltk.stem import PorterStemmer

# Download NLTK data (Run only once)
nltk.download('punkt')

# Create Porter Stemmer object
stemmer = PorterStemmer()

# List of words
words = [
    "playing",
    "studies",
    "running",
    "connected",
    "computers",
    "happiness",
    "writing",
    "flying",
    "walking",
    "better"
]

print("Original Word\tStemmed Word")
print("-" * 35)

# Perform stemming
for word in words:
    stem = stemmer.stem(word)
    print(f"{word}\t\t{stem}")