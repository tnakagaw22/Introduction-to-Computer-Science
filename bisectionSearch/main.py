# age = input("What is your age? ")
# print ("Your age is: " + age)



def guessNumber(min, max):
    midpoint = (max - min) / 2
    guess = int(min + midpoint)
    print (guess)
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if answer == 'c':
        print("Game over. Your secret number was: " + str(guess))
    elif answer == 'h':
        guessNumber(min, guess)
    elif answer == 'l':
        guessNumber(guess, max)


min = 0
max = 100
guessNumber(min, max)
