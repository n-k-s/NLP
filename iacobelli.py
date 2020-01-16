# for i in range(0,10):
#     print(i)
# for even in [2,4,6,8,10,12,14,16,18,20]:
#     print (even)
#     print(even/2)
# a = [1,2,4,5]
# a.append(10)
# print(a)
# a.append([2,2,2,2,2,2])
# a[5][2] = [1,1,1,1,1]
# print(a)
######
# import sys
# print(sys.argv[1])
########### lists 1
# a = [1, 2, 3, 4, 5, 6]
# b = ["hello", "how", "are", "you"]
# for i in range(0, len(b)):
#     print(b[i])
# for i in b:
#     print(i)
# b[1:4] #from 1 up to 4
# b[-1] #last element
# b[:3] #all elements up to 3 inclusive
# b[2:] #from 2 onwards
# b[-2] #last two elements
# c = a + b
######## lists 2
#a = [1,2,3,4,5,6]
# b =[]
# for i in a:
#     b.append(i**2)
# b=[i**2 for i in a]
# print(b)
#
# a = '''the dog bit the man on the oon when eating hot dog'''
# print(a.split(" "))
# text = "hello there I love to say Hi! That's why I like the beach"
# tl = text.split(" ")
# print(tl)
# tl[0].replace("h","H")
# clean_text = [i.replace("!","").replace("'","") for i in tl]
# print(clean_text)
############ list comprehensions
# a = [1,2,3,4,5,6,7,8,9,10]
# b = [i for i in a if i > 5]
# print(b)


############# dictionaries
# a = [{"title":"War and peace", "author":"Leo Tolstoi"} ,{"title":"Blindness", "author":"Jose Saramago"}, {"title":"Don Quixote", "author":"M de Cervantes"}]
# b = {"title":"Blindness", "author":"Jose Saramago"}
# print(a)
# for book in a:
#     print(book["author"])
# #b.has_key("author") #removed in python 3
# print("author" in b)
# b["author"]="Nolan Shikanai"
# print(b)
# b["number of pages"] = 298
# print(b)

# text = "hello there how are you today. Are you okay there"
# # a = text.split(" ")
# # counts = {}
# # for w in a:
# #     if w in counts:
# #         counts[w] += 1
# #     else:
# #         counts[w] = 1
# # print(counts)


########### files
# f = open("expenses.txt")
#
# fString = f.read()
# lines = fString.split("\n")
# total = 0
# o = open("out_exp.txt", "w")
# for tr in lines:
#     name,price = tr.split(",")
#     total += float(price)
#     print(float(price))
#     o.write("Processing " + name + "\n")
# print(total)
# o.write("total is " + str(total))
# o.close()
# f.close()

##### functions with word count


# def file2list(filename):
#     f = open(filename)
#     fStr = f.read()
#     lines = fStr.split(" ")
#     f.close()
#     return lines
#
# def countWords(lWords):
#     d = {}
#     for w in lWords:
#         if w in d:
#             d[w] += 1
#         else:
#             d[w] = 1
#     return d
#
# a = file2list("dreamspeech.txt")
# wc = countWords(a)
# print(wc)

############# modules

##########
from pprint import pprint
from collections import Counter


#########
def file2list(filename):
    return open(filename).read().split(" ")

def countWords(lWords):
    return Counter(lWords)

a = file2list("dreamspeech.txt")
wc = countWords(a)

pprint(wc.most_common(10))
pprint(wc["freedom"])

############## coding math equations

#
# def factorial(n):
#     temp = 1
#     for i in range(1, n + 1):
#         temp *= i
#     return temp
# print(factorial(5))
#
# def summationFactorial(n):
#     tempSum = 0.0
#     for i in range(0, n):
#         tempSum += 1.0 / float(factorial(i))
#     return tempSum
# print(summationFactorial(12))
#
# def avg(x):
#     temp = 0
#     for i in range(0, len(x)):
#         temp += x[i]
#     return 1.0/len(x) * temp
#
# print(avg([1.0,2.0,3.0]))
#
# def var(X):
#     temp = 0.0
#     for i in X:
#         for j in X:
#             temp += (1.0/2.0) * (i-j)**2
#     return temp * 1.0/len(X)**2
#
# print(var([1.1,2.3,4.0]))