import re
import pprint
f = open("grammar.txt")

#####i.match([#].*)
a = ""

# putting the file in a string that doesn't start with a #
for i in f:
    if (i[0] != "#"):
        a += i
print(a)

myList = a.split("\n")




#
# b = [i for i in a if ]
#
# b=[i**2 for i in a]
# print(a)
















f.close()