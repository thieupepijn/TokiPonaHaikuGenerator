from TokiPonaWoord import *
from Util import *

class Sentence(object):

 def __init__(self, allwords, numberofsyllables):
    self.words = self.getwoorden(allwords, numberofsyllables)

 def getwoorden(self, words, numberofsyllables):
    if (numberofsyllables == 5):
     threesyllablewords = list(filter(lambda w: TokiPonaWoord.SyllablesEqualTo(w,3) , words))
     word1 = Util.ChooseRandomItem(threesyllablewords).word 
     twosyllablewords = list(filter(lambda w: TokiPonaWoord.SyllablesEqualTo(w,2) , words))
     word2 = Util.ChooseRandomItem(twosyllablewords).word 
     return [word1, word2]
    elif(numberofsyllables == 7):
     twosyllablewords = list(filter(lambda w: TokiPonaWoord.SyllablesEqualTo(w,2) , words))
     threesyllablewords = list(filter(lambda w: TokiPonaWoord.SyllablesEqualTo(w,3) , words))
     word1 = Util.ChooseRandomItem(twosyllablewords).word 
     word2 = Util.ChooseRandomItem(threesyllablewords).word 
     word3 = Util.ChooseRandomItem(twosyllablewords).word 
     return [word1, word2, word3]         

 
   
