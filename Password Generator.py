#generate password for user depending on selected strength
#weak passwords will pick a random word from norvig's dictionary and add a random number
#medium passwords will pick a random word and include characters and numbers in a random order 
#strong passwords will be a random mix of upper and lower case letter, numbers, and symbols
#will generate a new password if the user wishes
#set() used to randomize order of medium and strong passwords each time

import string #used to get string of ascii character
import random

norvig_dic = open("Dictionary.rtf", 'r') #uses words from Norvig's dictionary for weak passwords
words = norvig_dic.readlines() #read dictionary

lower_letters = string.ascii_lowercase #string of lowercase letters
upper_letters = string.ascii_uppercase #string of uppercae letters
symbols = string.punctuation #string of symbols


def password_gen():

    #following three variables will generate a random assortment & random length of corresponding character type each time the function is called
    random_lower = random.sample(lower_letters, random.randint(3,int(len(lower_letters)/4)))
    random_upper = random.sample(upper_letters, random.randint(4,int(len(upper_letters)/2)))
    random_symbols = random.sample(symbols, random.randint(2,int(len(symbols)/6)))

    random_num = random.randint(1,9999)
    #random word picked from dictionary and stripped
    random_word = words[random.randint(10,267759)]
    random_word = random_word.replace('\\', '').strip().title()

    #prompts user to enter the desired strength of their generated password
    strength = input("\nWould you like a weak, medium, or strong password? ")

    if strength.lower().startswith('w'):
        password = random_word + str(random_num)
        print ("Your password is '" + password + "'")
        diff_pword = input("Would you like a different password? ")
        if diff_pword.lower().startswith('y'):
            password_gen()

    elif strength.lower().startswith('m'):
        password = [('').join(random_lower), str(random_num), random_word]
        print ("Your password is '" + ('').join(list(set(password))) + "'")
        diff_pword = input("Would you like a different password? ")
        if diff_pword.lower().startswith('y'):
            password_gen()

    elif strength.lower().startswith('s'):
        letter_symbols = random_lower + random_upper + random_symbols
        password = ('').join(list(set(letter_symbols))) + str(random_num)
        print("Your password is '" + password + "'")
        diff_pword = input("Would you like a different password? ")
        if diff_pword.lower().startswith('y'):
            password_gen()

    else:
        print("Invalid input. Password may be weak, medium or strong.")
        password_gen()


password_gen()
norvig_dic.close()