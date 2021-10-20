##I attempt to guess a number using the key pressed by the user to enter the game each key value
##has its own assigned value shuffled stored in the dictionary.

keys = {'0': 8, '1':7, '2': 1, '3': 0, '4':9, '5':4, '6':2, '7':5, '8':3, '9': 6}
try:
    #this try block is to prevent user from entering a character
    pressedKey = int(input('We guess a number you try to find it, press any key and press enter to continue: '))
except ValueError as error:
    print('Check input: ', error)
else:
    guess = keys[str(pressedKey)]
    guessedValue = False
    while(guessedValue == False):
        cuGuess = int(input('Enter guess'))
        if cuGuess == guess:
            guessedValue = True
    print("Guessed right the number was {}..congrats".format(guess))
