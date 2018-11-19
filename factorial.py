number = 5

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number -1)

result = factorial(5)
print(result)


def iterPower(base, exp):
    result = 0
    while exp > 0:
        if result == 0:
            result = base * base
        else:
            result = result * base
        exp = exp - 1
    if exp == 0:
        return 1
    else:
        return base * iterPower(base, exp - 1)

result = iterPower(3,5)
print(result)
       