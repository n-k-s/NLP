import math

def avg(X):
    tempAvg = 0
    for i in range(0, len(X)):
        tempAvg += X[i]
    return 1.0 / len(X) * tempAvg

def l_sqr(X):
    b = []
    b = [i ** 2 for i in X]
    return b

def var(X):
    numAvg = avg(X)
    sum = 0
    a = [i - numAvg for i in X]
    b = l_sqr(a)
    c = math.fsum(b)
    return (c / len(X))

# print(avg([23,32,43,54]) == 38.0)
# print(sum(l_sqr([23,32,43,54])) == 6318)
# print(var([23, 32, 43, 54]) == 135.5)