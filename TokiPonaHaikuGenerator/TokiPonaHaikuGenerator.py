from TokiPonaWoord import *
from Util import *
from Sentence import *

dictionaryFile = open('TokiPonaDictionary.txt')
header = dictionaryFile.readline()

items = dictionaryFile.readlines()
items = [i for i in items if i != '\n']

sentence1 = Sentence(items, 5)
sentence2 = Sentence(items, 7)
sentence3 = Sentence(items, 5)


print(str.join(' ', sentence1.words))
print(str.join(' ', sentence2.words))
print(str.join(' ', sentence3.words))