class TokiPonaWoord(object):
   


 def __init__(self, line):
  items = line.split(';');
  self.word = items[0]
  self.syllables = int(items[1])
 
 @staticmethod
 def SyllablesEqualTo(woord, syllables):
  return TokiPonaWoord(woord).syllables == syllables





