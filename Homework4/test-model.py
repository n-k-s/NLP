#!/usr/bin/env python3
""" n-gram models """
__author__ = "Nolan Shikanai"

from collections import Counter
import collections
import re
from pprint import pprint
from sys import argv


def ngrams(text, n):
    return [' '.join(text[i:i + n]) for i in range(len(text) - n + 1)]


def splitToSentences(text):
    return re.split("[.!?][ ]|[\r\n]+|[.]$", text)


def removeEmpty(theList):
    for i in theList:
        if len(i) == 0:
            theList.remove(i)
    return theList


def listOfLists(theList):
    # takes a list, splits on spaces, and makes a list of lists
    a = []
    for i in theList:
        b = i.split()
        a.append(b)
    return a


triLamda = .75
biLamda = .20
uniLamda = .05

# argv 0 program name, 1 model file, 2 sentences file
# modelFile = open(argv[1], encoding="utf8")
# sentencesFile = open(argv[2], encoding="utf8")
modelFile = open("a.txt")
sentences = open("sentences-file.txt").read()

splitSentences = splitToSentences(sentences)
splitSentences = removeEmpty(splitSentences)
splitSentences = listOfLists(splitSentences)
unigram = []
bigram = []
trigram = []

for i in splitSentences:
    unigram.append(ngrams(i, 1))
for i in splitSentences:
    bigram.append(ngrams(i, 2))
for i in splitSentences:
    trigram.append(ngrams(i, 3))

unigramStart = 0
unigramEnd = 0
uniEnd = False
bigramStart = 0
bigramEnd = 0
biEnd = False
trigramStart = 0

triEnd = False


# gets position of the unigrams, bigrams, and trigrams
for n, i in enumerate(modelFile):
    if len(i.split()) != 2 and uniEnd == False:
        unigramEnd = n
        bigramStart = (n + 1)
        uniEnd = True
    if len(i.split()) != 3 and biEnd == False and uniEnd == True:
        bigramEnd = n
        trigramStart = n + 1
        biEnd = True


print("Unigram: " + str(unigramStart) + " " + str(unigramEnd))
print("bigram: " + str(bigramStart) + " " + str(bigramEnd))
print("trigram: " + str(trigramStart) + " through end of file")

# calculate numbers. I'm so fucking tired

