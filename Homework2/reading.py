import re
import pprint
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
        if (i[0] not in grammarDictionary):
            grammarDictionary[i[0]] = [i[1]]
        else:
            grammarDictionary[i[0]].append(i[1])
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
    newList = popUseless(newList)
    return listToDict(newList)
################## END OF FILE FORMATTING#########################
f = open("grammar.txt")
myDict = fileFormatting(f)


pprint.pprint(myDict)





















f.close()