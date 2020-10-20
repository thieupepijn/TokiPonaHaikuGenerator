from TokiPonaWoord import *
from Util import *

class Sentence(object):

 def __init__(self, allwords, numberofsyllables):
    self.words = self.getwoorden(allwords, numberofsyllables)

 def getwoorden(self, words, numberofsyllables):
   sentencesyllables = 0
   output = []
   while sentencesyllables < numberofsyllables:
    words = list(filter(lambda w: TokiPonaWoord.SyllablesEqualOrLessThan(w,numberofsyllables - sentencesyllables), words))
    word = Util.ChooseRandomItem(words)
    words.remove(word)
    output.append(TokiPonaWoord(word).word)
    sentencesyllables = sentencesyllables + TokiPonaWoord(word).syllables
   return output
   
 
   
