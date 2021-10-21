"""I attempt to generate a pseudo random number by asking the user to press any number in order to enter the game
This number is what determines the guessed key word from the dictionary below each number has its owned assigned number"""

keys = {'0': 8, '1':7, '2': 1, '3': 0, '4':9, '5':4, '6':2, '7':5, '8':3, '9': 6}
try:
    #this try block is to prevent user from entering a character
    pressedKey = int(input('We guess a number you try to find it, press any number then press enter to continue: '))
except ValueError as error:
    print('Check input: ', error)
else:
    guess = keys[str(pressedKey)]
    guessedValue = False
    while(guessedValue == False):
        currentGuess = int(input('Enter guess'))
        if currentGuess == guess:
            guessedValue = True
    print("Guessed right the number was {}..congrats".format(guess))
