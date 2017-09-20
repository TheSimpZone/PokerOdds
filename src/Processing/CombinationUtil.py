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