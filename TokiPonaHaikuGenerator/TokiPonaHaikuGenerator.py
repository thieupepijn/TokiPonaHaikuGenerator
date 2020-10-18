from TokiPonaWoord import *
from Util import *
from Sentence import *

dictionaryFile = open('D:\Matthieu\ThieuProgs\Python\TokiPona\Data\TokiPonaDictionary.txt')
header = dictionaryFile.readline()

items = dictionaryFile.readlines()
items = [i for i in items if i != '\n']

#woord = Util.ChooseRandomItem(items)

#print(woord.woord)
#print(woord.syllables)

sentence = Sentence(items, 5)

print(sentence.sentencewoorden[0])
print(sentence.sentencewoorden[1])
