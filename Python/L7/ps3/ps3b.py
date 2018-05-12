from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
#comphand = deal_hand(HAND_SIZE)
sumcompscore = 0
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    global HAND_SIZE
    display_hand(hand)
    return checkhand(HAND_SIZE, hand)
    #print 'Your valid word to pick is: ', validwords[0]

def checkhand(n, hand):
    global validwords
    validwords = []
    global word
    for x in range(n, 1, -1):
        checkword(x, hand)
    if not validwords:
        return False
    else:
        word = validwords[0]
        return word


def checkword(n, hand):
    global handperms
    global validwords
    handperms = get_perms(hand, n)
    attempt = len(handperms)
    print 'Calculating best word with', n, 'letters' 
    for x in handperms:
        if x not in word_list:
            #attempt -= 1
            #print 'nope!', attempt
            pass
        else:
            validwords += [x]
            break
     
     

# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    global sumcompscore
    #global comphand
    global wordscore
    word = comp_choose_word(hand, word_list)
    if word == False:
        print 'No more valid words, Goodbye!'
        print 'Total: ', sumcompscore, 'points'
        return play_game(word_list)
    else:
        sumcompscore = sumcompscore + get_word_score(word, HAND_SIZE)
        print '"'+ word +'"', 'earned', wordscore, 'points.', 'Total:', sumcompscore, 'points.'
        hand = update_hand(hand, word)
        comphand = hand
    
    #print 'Total: ', sumcompscore, 'points'
    display_hand(hand)
    comp_play_hand(hand, word_list)
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    gametype = raw_input('Enter n for new random hand, r to replay the last hand and e to exit the game: ')
    global myhand
    global sumwordscore
    sumwordscore = 0
    if gametype == 'n':
        newhand = deal_hand(HAND_SIZE)
        myhand = newhand
        comptype = raw_input('Enter u to play single player and c to have the computer play: ')
        if comptype == 'u':
            play_hand(newhand, word_list)
        elif comptype == 'c':
            comp_play_hand(newhand, word_list)
        else:
            print 'Please enter a valid option.'
            play_game(word_list)
    elif gametype == 'r':
        comptype = raw_input('Enter u to play single player and c to have the computer play: ')  
        if comptype == 'u':
            play_hand(myhand, word_list)
        elif comptype == 'c':
            comp_play_hand(myhand, word_list)
        else:
            print 'Please enter a valid option.'
            play_game(word_list)
    elif gametype =='e':
        print 'Exiting the game, goodbye.'
        return
    else:
        print 'Please enter a valid option.'
        play_game(word_list)
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    
