#!/usr/bin/env python3
""" PMI """
__author__="Nolan Shikanai"

from collections import Counter
import collections
import re
from pprint import pprint
from sys import argv

def fileReading(fileName):
    with open(fileName) as i:
        c = i.read().lower().replace("`","").replace("'s","").replace("(","").replace(")","").replace(";","").replace(":","").split()
    return c
def ngrams(text, n):
    return ['_'.join(text[i:i + n]) for i in range(len(text) - n + 1)]

def writeDictToFileInOrder(dictionary):
    for i in dictionary.most_common():
        toFile.write(i[0] + "\t" + str(i[1]) + "\n")
def countWords(dictionary):
    numberOfWords = 0
    for i in dictionary.values():
        numberOfWords += i
    return numberOfWords
######################

# argv 0 program name, 1 filename, 2 number of sentences
importFile = argv[1]
exportFile = argv[2]
c = fileReading(importFile)
biGrams = ngrams(c, 2)
biGrams = collections.Counter(biGrams)
c = collections.Counter(c)
toFile = open(exportFile, "w")
wordCount = countWords(c)
#uniqueWords = len(c)
writeDictToFileInOrder(c)
writeDictToFileInOrder(biGrams)

toFile.write("@total@" + "\t" + str(wordCount))

toFile.close()