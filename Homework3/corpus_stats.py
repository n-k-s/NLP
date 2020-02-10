from collections import Counter
import collections
import re
from pprint import pprint
from sys import argv


# moviereviews.txt
def fileReading(fileName):
    with open(fileName) as i:
        c = i.read().lower().replace("(","").replace(")","").split()
    return c

def ngrams(text, n):
    return [' '.join(text[i:i + n]) for i in range(len(text) - n + 1)]


######################

# argv 0 program name, 1 filename, 2 number of sentences
importFile = argv[1]
exportFile = argv[2]
c = fileReading(importFile)
#c = c.lower()
biGrams = ngrams(c, 2)
biGrams = collections.Counter(biGrams)
c = collections.Counter(c)
wordCount = 0
for i in c:
    wordCount += c[i]
uniqueWords = len(c)
outputString = ""

for i in c.most_common():
    outputString += i[0] + "\t" + str(i[1]) + "\n"
for i in biGrams.most_common():
    outputString += i[0] + "\t" + str(i[1]) + "\n"
outputString = re.sub(" ", "_", outputString)
outputString += "@@@total@@@" + "\t" + str(wordCount)
#print(outputString)
toFile = open(exportFile, "w")
toFile.write(outputString)
toFile.close()
# pprint(c)
