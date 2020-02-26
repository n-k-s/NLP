#!/usr/bin/env python3
""" n-gram models """
__author__ = "Nolan Shikanai"

from collections import Counter
import collections
import re
from pprint import pprint
from sys import argv

def splitToSentences(text):
    return re.split("[.!?][ ]|[\r\n]+|[.]$", text)
def removeEmpty(list):
    for i in list:
        if len(i) == 0:
            list.remove(i)
    return list


triLamda = .75
biLamda = .20
uniLamda = .05

# argv 0 program name, 1 model file, 2 sentences file
# modelFile = open(argv[1], encoding="utf8")
# sentencesFile = open(argv[2], encoding="utf8")
modelFile = open("a.txt").read()
sentences = open("sentences-file.txt").read()

splitSentences = splitToSentences(sentences)
splitSentences = removeEmpty(splitSentences)



print(splitSentences)


