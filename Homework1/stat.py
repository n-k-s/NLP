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
    return 1
