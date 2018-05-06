from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
comphand = deal_hand(HAND_SIZE)
testhand = {'a':1, 's':2}
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    global HAND_SIZE
    display_hand(testhand)
    handperms = get_perms(testhand, 3)
    print 'length of perms', len(handperms)
    print 'Type is', type(handperms)
    checkword()

def checkword():
#    newperms = get_perms(comphand, (HAND_SIZE - 1))
    handperms = get_perms(comphand, (HAND_SIZE))
    validwords = []
    for x in handperms:
        if is_valid_word(x, comphand, word_list) == False:
            pass
        else:
            print 'Is True'
            validwords += [x]
            print validwords
#    checkword()

        
   #for s in range(0,HAND_SIZE):
   #     is_valid_word(get_perms(comphand, s), comphand, word_list)
   #     if True:
   #         print 'We have a winner!', s, get_perms(comphand, s)
    


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
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
    comp_choose_word(comphand,word_list)
    
