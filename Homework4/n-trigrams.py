#!/usr/bin/env python3
""" n-trigrams """
__author__ = "Nolan Shikanai"

from collections import Counter
import collections
import re
from pprint import pprint
from sys import argv


def ngrams(text, n):
    return [' '.join(text[i:i + n]) for i in range(len(text) - n + 1)]


def purgeEmpty(list):
    a = []
    for i in list:
        if len(i) > 0:
            a.append(i)
    return a


# argv 0 program name, 1 input file, 2 output file

importFile = open(argv[1])
exportFile = argv[2]
a = ""
for i in importFile:
    a += i
b = re.split("[.][ ]|[\r\n]+", a)

b = purgeEmpty(b)
pprint(b)
print(len(b))
print()
# print(b[-1])
# export = open(exportFile, "w")
#
# export.write("")
#
#
#
# export.close()
importFile.close()
