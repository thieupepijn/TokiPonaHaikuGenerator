from TokiPonaWoord import *
from Util import *

class Sentence(object):

 def __init__(self, woorden, syllables):
    self.sentencewoorden = self.getwoorden(woorden, syllables)

 def getwoorden(self, woorden, syllables):
    if (syllables == 5):
     threesyllablewords = list(filter(lambda w: Util.SyllablesEqualTo(w, 3), woorden))
     woord1 = Util.ChooseRandomItem(threesyllablewords).woord 
     twosyllablewords = list(filter(lambda w: Util.SyllablesEqualTo(w, 2), woorden))
     woord2 = Util.ChooseRandomItem(twosyllablewords).woord 
     return [woord1, woord2]
    elif(syllables == 7):
     return []
     
              

 
   
