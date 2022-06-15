# ## guess number

import random

randomNo  = random.randint(1,10)
# ##print(randomNo)       ## this will show the which random number module has choosed 
userGuess = None      ## this is define None so that this will not throw error when the loop enters first it will check its defined or not if its not then it will throw error (NameError: name 'userGuess' is not defined)
guesses = 0

while userGuess != randomNo:
    userGuess = int(input("Enter number : \n"))
    guesses += 1

    if userGuess == randomNo:
        print("WIN! you guessed the right number ")
    else :
        if userGuess > randomNo:
            print("You guessed the wrong number... enter a smaller number")
        else:
            print("You guessed the wrong number.. enter a larger number")

print(f"You Guessed The Number in {guesses} Guesses")
