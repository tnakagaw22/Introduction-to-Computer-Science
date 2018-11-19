def countVowels(s):
    counter = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        if s[i] in vowels:
            counter = counter + 1

    return counter

# countVowels('feiwafewf')


def findBob(s):
    counter = 0
    bob = 'bob'
    for i in range(len(s) - len(bob) + 1):
        firstThree = s[i] + s[i + 1] + s[i + 2]
        if firstThree == bob:
            counter = counter + 1

    print(counter)


# findBob('feiwboboblfew')
import string

def findOrderString(s):
    longestOrderedStrings = ""
    tempCharacters = []
    for i in s:
        tempCharacters.append(i)
        tempCharacterString = ''.join(tempCharacters)
        if ''.join(sorted(tempCharacters)) != tempCharacterString:
            if len(tempCharacterString[:-1]) > len(longestOrderedStrings):
                longestOrderedStrings = tempCharacterString[:-1]
            tempCharacters.clear()
            tempCharacters.append(i)
        elif len(tempCharacterString) > len(longestOrderedStrings):
            longestOrderedStrings = tempCharacterString

    return longestOrderedStrings
        
findOrderString('rztlsbpareuuovdbljcpilrg')

