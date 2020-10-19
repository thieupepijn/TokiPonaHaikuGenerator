from TokiPonaWoord import *
from Util import *

class Sentence(object):

 def __init__(self, woorden, syllables):
    self.sentencewoorden = self.getwoorden(woorden, syllables)

 def getwoorden(self, woorden, syllables):
    currentsyllables = 0
    tpw1 = Util.ChooseRandomItem(woorden)
    woord1 = tpw1.woord
    currentsyllables = tpw1.syllables
    syllables = 2 #int(syllables) - int(currentsyllables)
    boe = list(filter(lambda w: Util.SyllablesEqualTo(w, syllables), woorden))   
    #boe = list(filter(None, woorden))
    woord2 = Util.ChooseRandomItem(woorden).woord 
    return [woord1, woord2]
 
   
