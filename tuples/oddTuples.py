def oddTuples(aTup):
    tupleToReturn = ()

    index = 0
    for x in aTup:
        index += 1
        if index % 2 == 0:
            continue
        else:
            tupleToReturn = tupleToReturn + (x,)
    
    print(tupleToReturn)
    return tupleToReturn

testTuple = (1, 3, 4, 3, 5)
result = oddTuples(testTuple)
# print(result)