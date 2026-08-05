import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
import nltk

# Download required resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The experienced engineer carefully designed the bridge."

words = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)

print("POS Tags:")
for word, tag in pos_tags:
    print(f"{word:15} {tag}")