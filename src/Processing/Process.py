import numpy as np
from Processing import CombinationUtil as comb

#write function to iterate through

#write function to compare 2 hands and return the better one. This can be used for both finding the true score of a 7 card hand and the winner of a showdown


def processTable(hands, table):
    __DECKSIZE__ = 52
    num=__DECKSIZE__
    deck = np.array(np.ones(__DECKSIZE__))
    
    for hand in hands:
        deck[hand[0]] = False
        deck[hand[1]] = False
        num-=2
    for card in table:
        deck[card] = False
        num-=1

    numToDraw = 5-len(table) #cards remaining to be drawn
    combinations = comb.getCombinations(deck, numToDraw, __DECKSIZE__) #returns every combination of x cards out of deck
    listCombs = list(combinations)

    playerCombs = list()    

    for i in range(0, len(hands)):
        playerCombs.append(comb.addCardsToCombinations(list(listCombs), hands[i], table))

    print(playerCombs)

processTable([(0,1),(2,3),(4,5),(6,7),(8,9)], [10,11,12,13])
