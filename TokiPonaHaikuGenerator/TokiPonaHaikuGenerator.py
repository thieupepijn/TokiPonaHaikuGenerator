from TokiPonaWoord import *
from random import *

dictionaryFile = open('D:\Matthieu\ThieuProgs\Python\TokiPona\Data\TokiPonaDictionary.txt')
header = dictionaryFile.readline()

items = dictionaryFile.readlines()
numberofitems = len(items)
index = randint(0, numberofitems)

woord = TokiPonaWoord(items[index])

print(woord.woord)
print(woord.syllables)
