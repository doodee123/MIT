# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
quizword = choose_word(wordlist)
numguess = 9
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def guessCheck():
    global guess
    guess = raw_input('Please guess a letter: ')
    if guess not in letters:
        print 'Oops, you picked an already used letter. '
        guessCheck()
    else:
        letters.remove(guess)
        isCorrect()
        return guess

def isCorrect():
    global numguess
    if guess not in quizword:
        numguess -= 1
        print 'Oops! That letter is not in my word', " ".join(hiddenword)
        print 'You have', numguess, 'guesses left.'
        updateBlanks()
        print " ".join(hiddenword)
    else:
        updateBlanks()
        if hiddenword != quizword:
            print 'Good guess: ', " ".join(hiddenword)
            print 'You have', numguess, 'guesses left.'
            print 'available letters: ', " ".join(letters)
        else:
            print 'Congratulations, you won!'
            return


def guessFun():
    wordlen = len(quizword)
    print 'I am thinking of a word that is', wordlen, 'characters long.'
    print '-------------------'
    print 'You have', numguess, 'guesses left.'
    print 'available letters: ', " ".join(letters)
    genBlanks()
    while numguess > 0:
        guessCheck()
    else:
        print 'Sorry, you loose. The word was', quizword

def genBlanks():
    global hiddenword
    hiddenword = ''
    for c in quizword:
        hiddenword += '_'
    return hiddenword


# Define a function to replace the blanks with the correct guess letters.
# This function should take the existing list/tuple with the blanks (hiddenword) and remove any spaces from it.
# You can then replace the blanks with the correct letters and re-add the spaces before returning for use.

def updateBlanks():
    global hiddenword
    hlist = list(hiddenword)
    print quizword
    for i, c in enumerate(quizword):
#        key = quizword.index(c)
        if c != guess:
            pass
        else:
            hlist[i] = c
    hiddenword = ''.join(hlist)
#            hiddenword = hiddenword[:key] + c + hiddenword[key+1:]
        
        
    




