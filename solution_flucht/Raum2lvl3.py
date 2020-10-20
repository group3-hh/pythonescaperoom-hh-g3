def run(chars):
    testlist = []
    charlist= list(chars)
    final = []
    print(len(charlist))
    for i in range(0, len(charlist)):
        print(testlist)
        testlist.append(charlist[i])
        charlist.pop(i)
        if testlist[0] not in charlist:
            final.append(testlist[0])
            charlist.insert(i, testlist[0])
            testlist = []
        else:
            charlist.insert(i, testlist[0])
            testlist = []

    result = "".join(final)
    return result
