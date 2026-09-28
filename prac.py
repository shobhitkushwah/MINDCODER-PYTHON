# ============================================================
# NLP PRACTICE PROGRAM
# ============================================================


# ------------------------------------------------------------
# 1. Basic Python Input
# ------------------------------------------------------------

a = int(input("Enter the value of a = "))
print("Value of a =", a)


# ------------------------------------------------------------
# 2. NLTK - Tokenization
# ------------------------------------------------------------

import nltk
from nltk.tokenize import word_tokenize

# Run this once if punkt is not installed
nltk.download("punkt")

text = "NLP helps computers understand human language."

words = word_tokenize(text)

print("\n========== NLTK ==========")
print("Original text:")
print(text)

print("\nTokens:")
print(words)


# ------------------------------------------------------------
# 3. TextBlob - Sentiment Analysis
# ------------------------------------------------------------

from textblob import TextBlob

text = "I really love this movie. It is amazing!"

blob = TextBlob(text)

print("\n========== TEXTBLOB ==========")
print("Text:")
print(text)

print("\nSentiment:")
print(blob.sentiment)

print("\nPolarity:")
print(blob.sentiment.polarity)

print("\nSubjectivity:")
print(blob.sentiment.subjectivity)


# ------------------------------------------------------------
# 4. Gensim - Word2Vec
# ------------------------------------------------------------

from gensim.models import Word2Vec

sentences = [
    ["king", "queen", "man", "woman"],
    ["king", "royal", "palace"],
    ["queen", "royal", "palace"],
    ["man", "boy", "father"],
    ["woman", "girl", "mother"]
]

model = Word2Vec(
    sentences,
    vector_size=50,
    window=2,
    min_count=1,
    workers=1
)

print("\n========== WORD2VEC ==========")

print("\nMost similar words to 'king':")
print(model.wv.most_similar("king", topn=3))

print("\nVector of 'king':")
print(model.wv["king"])


# ------------------------------------------------------------
# 5. spaCy - Named Entity Recognition
# ------------------------------------------------------------

import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple was founded by Steve Jobs in California."

doc = nlp(text)

print("\n========== SPACY NER ==========")

print("\nOriginal text:")
print(text)

print("\nEntities:")

for entity in doc.ents:
    print(entity.text, "->", entity.label_)


# ------------------------------------------------------------
# 6. Hugging Face Transformers - Sentiment Analysis
# ------------------------------------------------------------

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

text = "I really enjoyed this movie!"

result = classifier(text)

print("\n========== TRANSFORMERS ==========")

print("\nText:")
print(text)

print("\nPrediction:")
print(result)


# ------------------------------------------------------------
# 7. Final Output
# ------------------------------------------------------------

print("\n================================")
print("       NLP PROGRAM FINISHED")
print("================================")