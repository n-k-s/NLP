import re
import pprint

#################### File Formatting ######################
def fileToString(f):
    a = ""
    for i in f:
        if (i[0] != "#"):
            a += i
    a = re.sub("[#].*", "", a)
    #a = re.sub("\t", " ", a)
    return a
def stringtoList(str):
    myList = str.split("\n")
    for i in myList:
        if (len(i) == 0):
            myList.remove(i)
    return myList
def popUseless(myList):
    for idx, i in enumerate(myList):
        i.pop(0)
    return(myList)
def fileFormatting(f):
    a = fileToString(f)
    myList = stringtoList(a)
    for i in myList:
        if (len(i) == 0):
            myList.remove(i)
    newList = []
    for idx, i in enumerate(myList):
        newList.append(i.split("\t"))
    newList = popUseless(newList)
    return newList
#########################################################



f = open("grammar.txt")
myList = fileFormatting(f)
pprint.pprint(myList)












f.close()