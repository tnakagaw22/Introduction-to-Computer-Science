import math

def area(numberOfSide, sideLength):
    return 0.25 * numberOfSide * sideLength**2 / math.tan(math.pi/numberOfSide)

def perimeter(numberOfSide, sideLength):
    return numberOfSide * sideLength

area(3, 3)
# import math

# def polysum(n,s):
#     return 0.25 * n * s**2 / math.tan * (math.pi/n) + n * s
# def area(n, s):
#     return 0.25 * n * s**2 / math.tan * (math.pi/n)

# def perimeter(n, s):
#     return n * s
