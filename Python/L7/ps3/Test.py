hand = {'p':1, 'y':1, 't':1, 'h':1, 'o':1, 'n':1}

def play_hand(hand):
    while any(hand) is True:
        print hand
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if word == '.':
            print 'Goodbye!'
            break
        else:
            if not (word == 'toy'):
                print 'Invalid word, Please try again.'
            else:
                print '"'+ word +'"', 'earned', 'points.'
                hand = {'p':1, 'h':1, 'n':1}
            
        
