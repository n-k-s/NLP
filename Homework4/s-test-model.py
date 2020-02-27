#!/usr/bin/env python3
""" n-gram models """
__author__ = "Nolan Shikanai"

import math
from collections import Counter
import collections
import re
from pprint import pprint
from sys import argv


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


# argv 0 program name, 1 model file, 2 sentences file
modelFile = open(argv[1], encoding="utf8")
sentences = open(argv[2], encoding="utf8").read()
bigramSentence = open(argv[2], encoding="utf8").read()

# modelFile = open("a.txt")
# sentences = open("sentences-file.txt").read()
# bigramSentence = open("sentences-file.txt").read()

bigramSentence = splitToSentences(bigramSentence)
bigramSentence = removeEmpty(bigramSentence)
bigramSentence = listOfLists(bigramSentence)


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
#print(bigram)
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

testingSentences = removeEmpty(splitToSentences(sentences))
sentenceCount = []

# print("Unigram: " + str(unigramStart) + " " + str(unigramEnd))
# print("bigram: " + str(bigramStart) + " " + str(bigramEnd))
# print("trigram: " + str(trigramStart) + " through end of file")
unigramCount = ""
bigramCount = ""
trigramCount = ""

# open(argv[1], encoding="utf8")
for n, i in enumerate(open("a.txt")):
    if n < unigramEnd:
        unigramCount += i
    elif n < bigramEnd:
        bigramCount += i
    else:
        trigramCount += i

# makes the unigrams into a dictionary
totalWords = 0
unigramDict = {}
uniFormatted = []
unigramCount = unigramCount.split("\n")
for i in unigramCount:
    uniFormatted.append(i.split("\t"))
for i in uniFormatted:
    if len(i) > 1:
        totalWords += int(i[1])
        unigramDict[i[0]] = int(i[1])

# print(splitSentences)


# bigram dict

bigramDict = {}
bigramCount = bigramCount.split('\n')
bigramCount = removeEmpty(bigramCount)
bigramPreDict = []
for i in bigramCount:
    bigramPreDict.append(i.split('\t'))
for i in bigramPreDict:
    if len(i) > 1:
        bigramDict[i[0]] = int(i[1])
# print(bigramPreDict)

# trigram dict
trigramDict = {}
trigramCount = trigramCount.split('\n')
trigramCount = removeEmpty(trigramCount)
trigramPreDict = []
for i in trigramCount:
    trigramPreDict.append(i.split('\t'))
trigramCount = 0
for i in trigramPreDict:
    if len(i) > 1:
        trigramCount += int(i[1])
        trigramDict[i[0]] = int(i[1])

endSentence(bigramSentence)
startSentence(bigramSentence)

endSentence(splitSentences)
startSentence(splitSentences)
startSentence(splitSentences)
sentenceBiGrams = []
sentenceBiGramsFixed = []
for n, i in enumerate(bigramSentence):
    sentenceBiGrams.append([])
    sentenceBiGrams[n].append(ngrams(i, 2))


sentenceTriGrams = []
sentenceTriGramsFixed = []
for n, i in enumerate(splitSentences):
    sentenceTriGrams.append([])
    sentenceTriGrams[n].append(ngrams(i, 3))


for i in range(len(sentenceBiGrams)):
    sentenceBiGramsFixed.append(sentenceBiGrams[i][0])
for i in range(len(sentenceTriGrams)):
    sentenceTriGramsFixed.append(sentenceTriGrams[i][0])

numberOfSentences = unigramDict["STOP"]
# print(sentenceTriGramsFixed)
triLamda = .6
biLamda = .4

# print(sentenceBiGramsFixed)
# print(sentenceTriGramsFixed)
for n, i in enumerate(sentenceBiGramsFixed):
    for nj, j in enumerate(i):
        bisplit = j.split()
        temp = bisplit[0]
        if (temp == "*"):
            if j in bigramDict:
                sentenceBiGramsFixed[n][nj] = (bigramDict[j] / numberOfSentences) * biLamda
            else:
                sentenceBiGramsFixed[n][nj] = 0.0
        elif temp in unigramDict and j in bigramDict:
            sentenceBiGramsFixed[n][nj] = (bigramDict[j] / unigramDict[temp]) * biLamda
        else:
            sentenceBiGramsFixed[n][nj] = 0

# print(sentenceBiGramsFixed)
for n, i in enumerate(sentenceTriGramsFixed):
    for nj, j in enumerate(i):
        jsplit = j.split()
        temp = jsplit[0] + " " + jsplit[1]
        if (temp == "* *"):
            if j in trigramDict:
                sentenceTriGramsFixed[n][nj] = (trigramDict[j] / numberOfSentences) * triLamda
            else:
                sentenceTriGramsFixed[n][nj] = 0
        elif temp in bigramDict and j in trigramDict:
            sentenceTriGramsFixed[n][nj] = (trigramDict[j] / bigramDict[temp]) * triLamda
        else:
            sentenceTriGramsFixed[n][nj] = 0
# print(len(sentenceTriGramsFixed))
# print(sentenceBiGramsFixed)
# print(sentenceTriGramsFixed)

finalProbability = []
for n, i in enumerate(sentenceTriGramsFixed):
    probability = 1
    for nj, j in enumerate(i):
        total = j + sentenceBiGramsFixed[n][nj]
        probability *= total
    finalProbability.append(probability)


last = sentences.split('.')
for n, i in enumerate(finalProbability):
    print("Probability of: ")
    print(last[n])
    print(i)
    print()
