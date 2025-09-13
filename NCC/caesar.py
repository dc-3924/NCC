import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import string,time

def matchPercent(text):
    s = 0

    tokens = word_tokenize(text.lower())
    cleaned_t = [w for w in tokens if w.isalpha()]

    for x in cleaned_t:
        if wordnet.synsets(x):
            s+=1

    return s * 100/ len(cleaned_t)

class DecryptCaesar:
    def __init__(self, text):
        self.text = text
        self.outcomes = self.generateOutcomes()

    def generateOutcomes(self):
        alphabet = string.ascii_uppercase
        outcomes = []
        for shift in range(26):
            s_text = ""
            for c in self.text:
                if c.isalpha():
                    new_c = alphabet[(alphabet.index(c.upper()) + shift) % 26]
                    s_text += new_c
                else:
                    s_text += c
            outcomes.append(s_text)
        return outcomes

    @property
    def decrypt(self) -> str:
        t = []
        for item in self.outcomes:
            t.append(matchPercent(item))
        print(self.outcomes[t.index(max(t))])
        print("\n" + " " + str(max(t)))

sentence = """
OLEP XLCNS 27ES 1959
EZ NLAELTY ZXPY
QCZX ACZQ. GLYOTGPC
DFMUPNE TYEPCNPAE

ESP DZGTPE XPDDLRP NZYELTYPO GLWFLMWP TYQZCXLETZY LYO L ELYELWTDTYR NWFP
NZYNPCYTYR ESP ZMUPNE HP LCP CPBFTCPO EZ CPNZGPC. 
"""

decrypt = DecryptCaesar(sentence)
decrypt.decrypt

"""
DATE MARCH 27TH 1959
TO CAPTAIN OMEN
FROM PROF. VANDIVER
SUBJECT INTERCEPT

THE SOVIET MESSAGE CONTAINED VALUABLE INFORMATION AND A TANTALISING CLUE
CONCERNING THE OBJECT WE ARE REQUIRED TO RECOVER. 


 70.37037037037037
"""
