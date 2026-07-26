# Import required libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK data (Run only once)
nltk.download('punkt')
nltk.download('wordnet')

# Input sentence
text = input("Enter a sentence: ")

# Tokenization
words = word_tokenize(text)

# Create Stemmer and Lemmatizer objects
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("\nWord\t\tStem\t\tLemma")
print("-" * 40)

# Perform stemming and lemmatization
for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print(f"{word}\t\t{stem}\t\t{lemma}")