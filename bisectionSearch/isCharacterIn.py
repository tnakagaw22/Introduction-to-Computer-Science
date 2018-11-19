def isIn(char, aStr):
    length = len(aStr)
    midpoint = int(length / 2)

    if midpoint == 0:
        return False
    elif char == aStr[midpoint]:
        return True
    else:
        return isIn(char, aStr[0:midpoint]) or isIn(char, aStr[midpoint:])
    print(length)

print(isIn("b", "test characterb"))