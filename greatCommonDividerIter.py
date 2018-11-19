def gcdIter(a,b):
    smaller = a
    bigger = b
    if a>b:
        smaller = b
        bigger = a
    
    # reminder = bigger % smaller
    # if bigger % smaller == 0:
    #     return smaller

    gcd = smaller
    while not (bigger % gcd == 0 and smaller % gcd == 0):
        gcd = gcd - 1

    return gcd

# gcdIter(304, 152)

def gcdRecur(a,b):
    smaller = b
    bigger = a
    if a<b:
        smaller = a
        bigger = b
    
    if smaller == 0:
        return a
    else:
        return gcdRecur(smaller,bigger % smaller)

result = gcdRecur(12, 9)
print(result)