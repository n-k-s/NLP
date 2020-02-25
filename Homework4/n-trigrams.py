#!/usr/bin/env python3
""" n-trigrams """
__author__ = "Nolan Shikanai"

from collections import Counter
import collections
import re
from pprint import pprint
from sys import argv


def ngrams(text, n):
    return [' '.join(text[i:i + n]) for i in range(len(text) - n + 1)]


def endSentence(list):
    newList = []
    for i in list:
        i.append("STOP")
        newList.append(i)
    return newList

def startSentence(list):
    for i in list:
        i.insert(0, "*")
    return list


def cleanNoise(theList):
    a = []
    for i in theList:
        i = i.replace("'s", "").replace("*", "").replace("~", "").replace(":", "").replace(",","").replace("_","").replace("--","")
        a.append(i)
    return a


def emptyListElement(theList):
    for i in theList:
        if len(i) == 0:
            theList.remove(i)
    return theList


def listOfLists(list):
    # takes a list, splits on spaces, and makes a list of lists
    a = []
    for i in list:
        b = i.split(" ")
        a.append(b)
    return a


def splitToSentences(text):
    return re.split("[.!?][ ]|[\r\n]+", text)


def clean(text):
    # takes the text as a long string, converts to lists divided by sentences, divided into words
    list = splitToSentences(text)
    list = cleanNoise(list)
    list = emptyListElement(list)
    list = listOfLists(list)
    for i in list:
        emptyListElement(i)
    return list


# argv 0 program name, 1 input file, 2 output file

importFile = open(argv[1], encoding="utf8")
exportFile = argv[2]
text = importFile.read()
sentences = clean(text)

# adds stop to the end
endSentence(sentences)
allgrams = ""
# unigrams
for i in sentences:
    for j in i:
        allgrams += j + " "
a = Counter(allgrams.split())
export = open(exportFile, "w", encoding="utf8")
# for i in a.most_common():
#     export.write(i[0] + "\t" + str(i[1]) + "\n")
startSentence(sentences)
bigrams = []
for i in sentences:
    bigrams.append(ngrams(i, 2))
for i in bigrams:
    for j in i:
        allgrams += j + " "
pprint(allgrams)





# bigrams = ngrams(bigram, 2)
# trigrams = ngrams(trigram, 3)




export.close()
importFile.close()
