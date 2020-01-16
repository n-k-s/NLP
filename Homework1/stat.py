import math


def avg(X):
    tempAvg = 0
    for i in range(0, len(X)):
        tempAvg += X[i]
    return 1.0 / len(X) * tempAvg


myNum = [1, 2, 3]
print(avg(myNum))


def l_sqr(X):
    b = []
    b = [i ** 2 for i in X]
    return b


print(l_sqr(myNum))


def var(X):
    print("In var")
    numAvg = avg(X)
    sum = 0
    a = [i - numAvg for i in X]
    b = l_sqr(a)
    c = math.fsum(b)
    return (c / len(X))

print(var([23, 32, 43, 54]) == 135.5)