import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

def matchPercent(text) -> float:
    s = 0

    tokens = word_tokenize(text.lower())
    cleaned_t = [w for w in tokens if w.isalpha()]

    if cleaned_t == 0:
        return 0

    for x in cleaned_t:
        if wordnet.synsets(x):
            s+=1

    return s * 100/ len(cleaned_t)

def modularInverse():
    pass