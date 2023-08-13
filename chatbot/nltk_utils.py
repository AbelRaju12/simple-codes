import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    pass

# a = "how are you?"
# print(a)
# a = tokenize(a)
# print(a)
# a = [stem(w) for w in ["organizing", "organizer", "organized"]]
# print(a)