from sys import argv
from collections import Counter

mylist = [i for i in argv]
if len(mylist) > 1:
    mylist.pop(0)
print(Counter(mylist))
dict = (Counter(mylist).most_common(1))
print(dict[0][0])


# dict = Counter([i for i in argv]).most_common(1)
# print(dict[0][0])