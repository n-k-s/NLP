from sys import argv
from collections import Counter

f = open(argv[1])
scriptString = f.read()
charCount = len(scriptString)
spaceCount = scriptString.count(" ")
newLineCount = scriptString.count("\n") + 1
scriptString = scriptString.lower()
scriptString = scriptString.replace(",","")
scriptList = scriptString.split(" ")
scriptDict = Counter(scriptList)

print("types:" + str(len(scriptDict)) + ", chars:" + str(charCount) + ", lines:" + str(newLineCount) + ".")