
def most_frequent(str1):
    myDict = {}
    for n in str1:
        keys = myDict.keys()
        if n in keys:
            myDict[n] += 1
        else:
            myDict[n] = 1
    return myDict
print(most_frequent('mississipi'))
