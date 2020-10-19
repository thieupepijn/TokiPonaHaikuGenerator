from TokiPonaWoord import *
from Util import *
from Sentence import *

dictionaryFile = open('D:\Matthieu\ThieuProgs\Python\TokiPona\Data\TokiPonaDictionary.txt')
header = dictionaryFile.readline()

items = dictionaryFile.readlines()
items = [i for i in items if i != '\n']

sentence = Sentence(items, 5)
print(str.join(' ', sentence.sentencewoorden))