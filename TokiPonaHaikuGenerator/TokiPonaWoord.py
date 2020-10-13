class TokiPonaWoord(object):
   


 def __init__(self, line):
    items = line.split(';');
    self.woord = items[0]
    self.syllables = items[1]




