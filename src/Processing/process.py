import numpy as np

def getCombinations(deck, numToDraw, numInDeck):
    if numToDraw == 0:
        yield ()
    elif numToDraw == 1:
        for i in range(0, numInDeck):
            if deck[i] == 1:
                yield (i,)
    else:
        for i in range(0, numInDeck):
            #print(i)
            if deck[i] == 1:
                deck[i] = 0
                for j in getCombinations(deck, numToDraw-1, i):
                    yield (i,) + j
                deck[i] = 1

def insertToTuple(tup, i, val):
    tupList = list(tup)
    tupList.insert(i, val)
    return tuple(tupList)


def insertToComb(c, val):
    #print(c)
    #print(val)
    #print("new call")
    for i in range(0, len(c)):
        if val < c[i]:
            continue
        else:
            c = insertToTuple(c, i, val)
            return c
    c = insertToTuple(c, len(c), val)
    return c
            

def addCardsToCombinations(combinations, hand, table):
    for i in range(0, len(combinations)):
        c = combinations[i]
        c = insertToComb(c, hand[0])
        c = insertToComb(c, hand[1])
        #print(c)
        for card in table:
            c = insertToComb(c, card)
        #print(c)
        combinations[i] = c
    return combinations

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
    combinations = getCombinations(deck, numToDraw, __DECKSIZE__) #returns every combination of x cards out of deck
    listCombs = list(combinations)

    playerCombs = list()    

    for i in range(0, len(hands)):
        playerCombs.append(addCardsToCombinations(list(listCombs), hands[i], table))

    print(playerCombs)

processTable([(0,1),(2,3),(4,5),(6,7),(8,9)], [10,11,12,13])
