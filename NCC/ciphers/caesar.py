import string
from NCC.utilities.utilities import matchPercent

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
    def decrypt(self) -> None:
        t = []
        for item in self.outcomes:
            t.append(matchPercent(item))
        print(self.outcomes[t.index(max(t))])
        print("\n" + " " + str(max(t)))

