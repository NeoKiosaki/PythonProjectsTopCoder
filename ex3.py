def isListOfInts(a):
    flag = True
    if type(a) is not list:
        raise ValueError("arg not of <list> type")
    else:
        for i in a:
            if type(i) is not int:
                flag = False
                break
    return flag


def testList(s):
    print (s, end='')
    print("-->", end='')
    print(isListOfInts(s))

testList([])
testList([1])
testList([1,2])
testList([0])
testList(['1'])
testList([1,'a'])
testList(['a',1])
testList([1, 1.])
testList([1., 1.])
testList((1,2))
