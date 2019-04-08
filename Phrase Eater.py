#Prints sentence with one less character each time

import string

chars = string.ascii_letters + string.punctuation

def phrase_eater(phrase):
    while phrase:
        if phrase[len(phrase)-1] in chars:
            print (phrase)
            phrase = phrase[:len(phrase)-1]
        else :
            phrase = phrase[:len(phrase)-1]

phrase_eater("Will this eat each letter?")
