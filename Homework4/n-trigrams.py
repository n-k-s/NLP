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

def cleanNoise(theList):
    a = []
    for i in theList:
        i = i.replace("'s", "").replace("*","").replace("~","")
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

def clean(text):
    list = splitToSentences(text)
    list = cleanNoise(list)
    list = emptyListElement(list)
    list = listOfLists(list)
    return list


# argv 0 program name, 1 input file, 2 output file

importFile = open(argv[1])
exportFile = argv[2]
text = importFile.read()
sentences = clean(re.split("[.!?][ ]|[\r\n]+", text))


pprint(sentences)

# print(b[-1])
# export = open(exportFile, "w")
#
# export.write("")
#
#
#
# export.close()
importFile.close()
