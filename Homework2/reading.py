import re
import pprint

def fileToString(f):
    a = ""
    for i in f:
        if (i[0] != "#"):
            a += i
    a = re.sub("[#].*", "", a)
    a = re.sub("\t", " ", a)

    return a

def stringtoList(str):
    myList = str.split("\n")
    for i in myList:
        if len(i) == 0:
            myList.remove(i)
    return myList


f = open("grammar.txt")



a = fileToString(f)
myList = stringtoList(a)
pprint.pprint(myList)













f.close()