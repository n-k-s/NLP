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
    for i in mySentence:
        if (i in dictionary):
            return False
    return True
def buildSentence(list, dict):
    # returns a list of words from the given list passed in
    return list[randrange(len(list))].split(" ")

################# END OF LOGIC ###################################

# argv 0 program name, 1 filename, 2 number of sentences
#f = open(argv[1])
#times = argv[2]
#print(times)


f = open("grammar.txt")
myDict = fileFormatting(f)
pprint.pprint(myDict)

sentence = buildSentence(myDict["ROOT"], myDict)
print(sentence)

sentence[0] = buildSentence(sentence[0], myDict)
print(sentence)

# while (not isTerminal(sentence, myDict)):
#     buildSentence(sentence[i])
#     i += 1
#     print(sentence)

























f.close()