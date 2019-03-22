# generates a random 4 digit number for user to guess
# prints the status of the guess (number of cows and bulls) 
# cow = right number in right position
# bull = right number in wrong position

import random

def cows_and_bulls():

    num_guesses = 1 #number of guesses user takes to get the number
    digit = str(random.randint(1000, 9999)) #converts the random digit to a string to make string comparisons
    print(digit)

    while True:
        print() #white space

        #number of cows and bulls returns to zero after each guess
        cows = 0 
        bulls = 0
        guess = input('Guess the four digit number: ') #prompts user to guess digit
        print('You guessed', guess)

        #if statement breaks while loop if user guessed the digit
        #calls play_again() function; runs cows_and_bulls if user says yes
        if guess == digit: 
            print('\nAwesome! You got it! =)')
            print('You took', num_guesses, 'tries.')
            play_again()
            break

        #else statement compares guess and digit and prints the status of the guess (# cows and bulls)
        else:
            for index in range(4):
                if guess[index] == digit[index]:
                    cows += 1
                elif guess[index] in digit:
                    bulls += 1
            num_guesses += 1
            print(cows, 'cows and', bulls, 'bulls')

#function called in main function to run game again
def play_again():

    another = input('\nDo you want to play again? Y/N ')
    if another.lower().startswith('y'):
        cows_and_bulls()

cows_and_bulls()    