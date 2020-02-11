#!/usr/bin/env python3
""" PMI """
__author__="Nolan Shikanai"

from collections import Counter
import collections
import re
from pprint import pprint
from sys import argv
import math

def regexMaker(word):
    return "^" + word + "\t"

def count(i):
    splitter = i.split("\t")
    return splitter[1].replace("\n","")

# argv 0 program name, 1 filename, 2 first word, 3 second word

bigramRegex = regexMaker(argv[2] + "_" + argv[3])
firstWordRegex = regexMaker(argv[2])
secondWordRegex = regexMaker(argv[3])

f = open(argv[1])
biGramWord = 0
totalWord = 0
firstWord = 0
secondWord = 0

for i in f:
    if(re.match(bigramRegex, i)):
        biGramWord = count(i)
    if(re.match("@total@", i)):
        totalWords = count(i)
    if(re.match(firstWordRegex, i)):
        firstWord = count(i)
    if (re.match(secondWordRegex, i)):
        secondWord = count(i)

print("bigram: " + biGramWord)
print("total words: " + totalWords)
print("first word: " + firstWord)
print("second word: " + secondWord)

pmi = math.log2((int(biGramWord) * 12) / (int(firstWord) * int(secondWord)))
print(pmi)


f.close()