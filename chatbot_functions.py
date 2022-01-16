import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

# takes the message and makes it into a list with each element being a separate word
def tokenize(sentence):
    return nltk.word_tokenize(sentence)


# finds the root word of each of the words in the list and puts them all in lowercase
def stem(word):
    return stemmer.stem(word.lower())


# gets the stemmed words and sees if the patterns inn the json file matches with any of the words in the message
def sack_of_words(tokenized_sentence, words):
    # stems each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # makes
    sack = np.zeros(len(words), dtype=np.float32)
    for index, w in enumerate(words):
        if w in sentence_words:
            sack[index] = 1

    return sack
