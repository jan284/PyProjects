#Game of mastermind that generates a random number for user to guess
#0 - number in that place is not correct
#1 - number in the wrong place
#2 - number in the right place

import random 

def greeting1():
    print("\nWelcome to Mastermind!")
    print("~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Guess the four digit number")
    print("The status of your guess will be printed in 0's, 1's, and 2's")
    print("0 - digit not in number\n1 - digit in the wrong place\n2 - digit in the right place")


def greeting2():
    print("\nWelcome to Mastermind!")
    print("~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Guess the four digit number")
    print("The status of your guess will be printed in 0's, and 1's")
    print("0 - digit in the wrong place\n1 - digit in the right place")


def mastermind():

    number = str(random.randint(1000, 9999)) #generate random number and store in variable
    #print(number)
    num_guesses = 0

    while True:
        guess = input("\nEnter guess (q to quit): ") #prompt user to enter 4 digit guess
        if guess.lower().startswith('q'):
            print("The number was", number)
            break
        status = [] #variable that will become 4 digit string that tells user if digits in guess are correct
        index = 0 #variable to iterate through guess

        #for loop checks each number in the user's guess against the randomly generated number
        for num in guess:
            if num not in number:
                status.append('0')
                index += 1
            elif num == number[index]:
                status.append('2')
                index += 1
            else:
                status.append('1')
                index += 1

        num_guesses += 1

        status_str = ('').join(status) #convert status list to a string
        print(status_str)
        if status_str == '2222': #ends while loop if guess is correct
            print("Awesome! You guessed it in", num_guesses, "tries!")
            break
        else:
            print("Not quite. Try again.")
        
    #starts another game of mastermind if user wishes
    another = input("\nDo you want to play again? ")
    if another.lower().startswith('y'):
        mastermind()
    else:
        print("\nGoodbye!")

#greeting1()
#mastermind()

#same as mastermind but does not let user know which numbers are correct
def mastermind_hard():

    number = str(random.randint(1000, 9999)) #generate random number and store in variable
    #print(number)
    num_guesses = 0

    while True:
        guess = input("\nEnter guess (q to quit): ") #prompt user to enter 4 digit guess
        if guess.lower().startswith('q'):
            print("The number was", number)
            break
        #following 3 int variables keep count of 0's, 1's, and 2's for each guess
        num_0 = 0
        num_1 = 0
        index = 0 #variable to iterate through guess

        #for loop checks each number in the user's guess against the randomly generated number
        for num in guess:
            if num == number[index]:
                num_1 += 1
                index += 1
            elif num in number:
                num_0 += 1
                index += 1
            else:
                index += 1

        num_guesses += 1

        print("Number of 0's =", num_0, "\nNumber of 1's =", num_1)
        if num_1 == 4: #ends while loop if guess is correct
            print("\nAwesome! You guessed it in", num_guesses, "tries!")
            break
        else:
            print("Not quite. Try again.")
        
    #starts another game of mastermind if user wishes
    another = input("\nDo you want to play again? ")
    if another.lower().startswith('y'):
        mastermind_hard()
    else:
        print("\nGoodbye!")

#greeting2()
#mastermind_hard()
