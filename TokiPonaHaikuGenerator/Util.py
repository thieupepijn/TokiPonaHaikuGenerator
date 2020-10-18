from random import *
from TokiPonaWoord import *

class Util:
   
 def ChooseRandomItem(items):
  numberofitems = len(items)
  index = randint(0, numberofitems-1)
  return TokiPonaWoord(items[index])

