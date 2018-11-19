# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "D:/repo/Introduction to Computer Science/hangman/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if len(lettersGuessed) == 0:
        return False

    lettersToGuess = list(secretWord)
    for secretWordLetter in secretWord:
        if secretWordLetter in lettersGuessed and secretWordLetter in lettersToGuess:
            lettersToGuess.remove(secretWordLetter)

    return len(lettersToGuess) == 0


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = []
    for index in range(0, len(secretWord)):
        guessedWord.append("_")

    for index in range(0, len(lettersGuessed)):
        for secretWordIndex in range(0, len(secretWord)):
            if secretWord[secretWordIndex] == lettersGuessed[index]:
                guessedWord[secretWordIndex] = lettersGuessed[index]
    #    if lettersGuessed[index] in secretWord:
    #         guessedWord.append(lettersGuessed[index])

    return ''.join(guessedWord)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    availableLetters = []
    alphabet = string.ascii_lowercase
    for character in alphabet:
        availableLetters.append(character)

    for letter in lettersGuessed:
        if letter in alphabet and letter in availableLetters:
            availableLetters.remove(letter)

    return ''.join(availableLetters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("secretWord contains " + str(len(secretWord)) + " letters")
    print("CHEAT: secretWord is " + secretWord)

    guessLimit = 8
    lettersGuessed = []
    guessCount = 0
    while isWordGuessed(secretWord, lettersGuessed) == False:

        if guessCount > guessLimit:
            print("Could not get the word within " + str(guessLimit) + " guesses. Game over.")
            break
        guess = input("Guess a letter of secretWord.")
        guessCount += 1

        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
        print(getGuessedWord(secretWord, lettersGuessed))
        print("available characters : " + str(getAvailableLetters(lettersGuessed)))

    if isWordGuessed(secretWord, lettersGuessed):
        print("All letters are guessed successfully")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
