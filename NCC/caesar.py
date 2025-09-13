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
NZYNPCYTYR ESP ZMUPNE HP LCP CPBFTCPO EZ CPNZGPC. ESP V3 TD MPWTPGPO EZ
MP ESP QTCDE DPCGTYR YFNWPLC AZHPCPO MZLE TY ESP DZGTPE QWPPE LYO TED
NLAELTY TD LY PIAPCTPYNPO ZQQTNPC. ESP NSZTNP ZQ ESTD MZLE XLJ TYOTNLEP
ESLE ESP DZGTPED TYEPYO EZ DELJ DFMXPCDPO QZC DZXP ETXP, LYO ESTD
NZYQTCXD XJ DFDATNTZY ESLE ESPJ OZ YZE SLGP RZZO TYEPWWTRPYNP NZYNPCYTYR
ESP WZNLETZY ZQ ESP ZMUPNE. RTGPY TED LAALCPYE OPDTRYLETZY LD L MPLNZY T
LX AFKKWPO ESLE ESPCP TD YZ DTRYLW QZC FD EZ QZWWZH. T HZFWO CPNZXXPYO
XZYTEZCTYR ESP DAPNECFX QZC FYPIAPNEPO LNETGTEJ YPLC ESP NCLDS DTEP. ZFC
CLOTZ CZZX DPYE XP ESP PYNWZDPO DTRYLW HSTNS TD MPWTPGPO EZ SLGP MPPY
ECLYDXTEEPO MJ ESP V3 ACTZC EZ OTGTYR. LD JZF ACPOTNEPO TE TD PYNCJAEPO,
MFE, TE LAAPLCD, ZYWJ WTRSEWJ, LYO T HTWW PYOPLGZFC EZ OPNTASPC TE
BFTNVWJ. XPLYHSTWP T HZFWO CPNZXXPYO ESLE HP TXACZGP DPNFCTEJ MJ STOTYR
ESP HZCO DECFNEFCP ZQ ZFC XPDDLRPD FDTYR ESP DELYOLCO 5 WPEEPC MWZNV
QZCXLE.
"""

decrypt = DecryptCaesar(sentence)
decrypt.decrypt
