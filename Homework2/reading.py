#!/usr/bin/env python3
""" Context Free Grammars """
__author__="Nolan Shikanai"

import re
import pprint
from random import randrange
from sys import argv
#################### File Formatting ######################
def fileToString(f):
    a = ""
    for i in f:
        if (i[0] != "#"):
            a += i
    a = re.sub("[#].*", "", a)
    return a
def stringtoList(str):
    #splits on the 1 and then removes no length lists
    myList = str.split("\n")
    for i in myList:
        if (len(i) == 0):
            myList.remove(i)
    return myList
def popUseless(myList):
    #removes the 1 at the start of the list
    for idx, i in enumerate(myList):
        i.pop(0)
    return(myList)

####### makes the dictionary from the formatted list
def listToDict(myList):
    grammarDictionary = {}
    for i in myList:
        if (i[0] == "1"):
            if (i[1] not in grammarDictionary):
                grammarDictionary[i[1]] = [i[2]]
            else:
                grammarDictionary[i[1]].append(i[2])
        else:
            if (i[1] not in grammarDictionary):
                grammarDictionary[i[1]] = [i[2]]
                for j in range(int(i[0]) - 1 ):
                    grammarDictionary[i[1]].append(i[2])
            else:
                for j in range(int(i[0])):
                    grammarDictionary[i[1]].append(i[2])

    return grammarDictionary

# the method that calls all the other formatting methods
def fileFormatting(f):
    #removes nothingness, creates a list within the list and splits on the tab character
    a = fileToString(f)
    myList = stringtoList(a)
    for i in myList:
        if (len(i) == 0):
            myList.remove(i)
    newList = []
    for idx, i in enumerate(myList):
        newList.append(i.split("\t"))
    return listToDict(newList)
################## END OF FILE FORMATTING#########################


################# Start of logic :^) #############################
def isTerminal(mySentence, dictionary):
    #takes in a list of words, checks each one
    for i in mySentence:
        if (i in dictionary):
            return False
    return True
def buildSentence(word, dict):
    # returns a list of words from the given list passed in
    #return list[randrange(len(list))].split(" ")
    # print("Being passed in ")
    # print(type(word))
    # print(word)
    if word not in dict:
        # print("not in dictionary")
        return word
    else:
        # returns a random string from the given dictionary key
        # print("in dictionary")
        # print(myDict[word][randrange(len(myDict[word]))])
        return(myDict[word][randrange(len(myDict[word]))])
def stringToListSplitterOnSpace(sentence):
    return sentence.split(" ")
def listToString(list):
    temp = ""
    for i in list:
        temp += i + " "
    return temp
def emptyElementInList(list):
    for i in list:
        if len(i) == 0:
            list.remove(i)
    return list
################# END OF LOGIC ###################################

# argv 0 program name, 1 filename, 2 number of sentences
#f = open(argv[1])
#times = argv[2]
#print(times)

f = open("grammar.txt")
myDict = fileFormatting(f)
pprint.pprint(myDict)

print("")
print("")
print("")
print("##### Building the initial sentence #####")

sentence = buildSentence("ROOT", myDict)
print(sentence)
a = stringToListSplitterOnSpace(sentence)

print("")
print("")
print("")
print("######## TESTING BUILDING SENTENCES ########")
sentenceAsList = stringToListSplitterOnSpace(sentence)
while not isTerminal(sentenceAsList, myDict):
    newSentence = ""
    sentenceAsList = stringToListSplitterOnSpace(sentence)
    # print(sentenceAsList)

    for i in sentenceAsList:
        temp = buildSentence(i, myDict)
        newSentence += temp + " "
    # print(newSentence)
    sentence = newSentence
    sentenceAsList = sentence.split(" ")


print("")
print("")
print("")
sentence = listToString(sentenceAsList)
print(sentence)



# while (not isTerminal(sentence, myDict)):
#     buildSentence(sentence[i])
#     i += 1
#     print(sentence)

























f.close()