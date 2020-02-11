#!/usr/bin/env python3
""" PMI """
__author__="Nolan Shikanai"

from collections import Counter
import collections
import re
from pprint import pprint
from sys import argv
# argv 0 program name, 1 filename, 2 first word, 3 second word
bigram = argv[2] + "_" + argv[3]
print(bigram)

f = open(argv[1])
for i in f:
    if (bigram in i):
        print("found " + i)








f.close()