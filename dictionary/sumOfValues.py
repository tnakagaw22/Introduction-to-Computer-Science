def how_many(aDict):
    values = aDict.values()
    sum = 0
    for value in values:
        sum += len(value)
    return sum

def biggest(aDict):
    result = ''
    max = 0
    for key, value in aDict.items():
        if len(value) > max:
            result = key
    return result

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# print(how_many(animals))
print(biggest(animals))