#full game of hangman
#random word from Norvig's dictionary is chosen as the word to guess
#user enters letters and progress is printed with each guess
#program ends when user guesses the word or when they have entered 6 incorrect guesses

norvig_dic = open("Dictionary.rtf", 'r')
words = norvig_dic.readlines()

import random
import string

def hangman():

    print("\nLet's play a game of Hangman!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    #chooses a random word from the dictionary (first word on line 10)
    random_word = words[random.randint(10,267759)]
    #stores random word in an immutable variable and removes backslash and whitespace
    ran_word = random_word.strip().replace('\\', '')

    #random word shouldn't be printed for final draft
    #print(ran_word)

    #creates variable containing all letters
    letters = string.ascii_letters

    #creates string of underscores to show number of letters in the word
    spaces = ''
    length = len(ran_word)
    while length:
        spaces += ('_ ')
        length -= 1
    print(spaces, '\n')

    #creates a list of underscores so changes can be made as letters are guessed
    spaces_list = spaces.split(' ')

    num_guesses = 0 #number of guesses made (not counting repeats nor correct guesses)
    guesses = [] #list of letters guessed

    #while loop continues to allow user input until user wins or loses 
    #(assumes user will input letters)
    guess = input('Guess a letter: ')
    print('')
    while True:

        if '_' not in spaces_list: 
            #breaks out of loop if all letters guessed before 6 incorrect tries used
            print('You win! =)')
            break

        elif len(guess) > 1:
            print('Invalid entry. ')
            guess = input('Enter 1 letter.')
            print('')

        elif guess not in letters:
            print('Invalid entry. ')
            guess = input('Try a letter.')
            print('')

        elif guess.upper() in guesses: 
            #tells user they already entered current guess
            print('You\'ve already guessed', "'" + guess.upper() + "'.")
            guess = input('Try another letter: ')
            print('')

        elif guess.upper() in ran_word: 
            #searches word for guessed letter and replaces underscore in spaces list with letter
            for letter in range(len(spaces_list)-1):
                if guess.upper() == ran_word[letter]:
                    spaces_list[letter] = guess.upper()
            #adds correct guess to guesses list and reassigns string of letters
            guesses.append(guess.upper())
            spaces = (' '.join(spaces_list)) 
            print(spaces) #displays word with revealed letters and underscores
            print('')

            #detects if current guess completed word
            if '_' not in spaces: 
                #breaks out of loop if all letters guessed before 6 tries used
                print('Awesome! You win! =)')
                break
            else:
                guess = input('Guess a letter: ')
                print('')

        else: 
            #else case for letters not in word (incorect guesses) nor guess list
            if num_guesses == 6: 
                #breaks out of loop when guess threshold is reached (6 incorrect guesses)
                print('Sorry. You lose. =(')
                print('The word was', ran_word)
                break
            else:
                #increases number of incorrect guesses by one and allows another guess
                guesses.append(guess.upper())
                num_guesses += 1
                print("'" + guess.upper() + "'", 'not in word.')
                print('You have', (6 - num_guesses), 'incorrect guesses left.')
                print(spaces)
                print('')
                guess = input('Guess a letter: ')
    #print(guesses)

    #starts another game depending on user input
    another = input('\nDo you want to play again, Y/N? ')
    if another.upper().startswith('Y'):
        hangman()
    else:
        print('\nThanks for playing.\nGoodbye!\n')

hangman()

norvig_dic.close()   