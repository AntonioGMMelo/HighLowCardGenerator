from applicationHLCG.RandomFunctions import *

def newGame(hlOption, numPlayersOption, dificultyOp, jokerOp):
    highOrLow = h(hlOption)
    numberOpponents = n(numPlayersOption)
    difficulty = d(dificultyOp)

    allDraws = []


    count = 0

    while count < numberOpponents + 1:

        playerDraw = drawCards(difficulty, jokerOp, allDraws)
        allDraws.append(playerDraw)

        count = count + 1

    #print(allDraws)

    countForCycles = 0


    if(highOrLow == "High Card"):
        savedNumber = [0, 0, 0]  # number of card, bonus value, position

        for x in allDraws:
            #print(countForCycles)
            #print(allDraws[countForCycles])
            #print(allDraws[countForCycles][0])

            if(allDraws[countForCycles][2] == True): #calhou joker

                return countForCycles, allDraws, numberOpponents, highOrLow

#            print(savedNumber[0])
#            print(allDraws[countForCycles][0])

            if (savedNumber[0] < allDraws[countForCycles][0]):
                savedNumber = [allDraws[countForCycles][0], allDraws[countForCycles][4], countForCycles]
            if (savedNumber[0] == allDraws[countForCycles][0]):
                if (savedNumber[1] < allDraws[countForCycles][4]):
                    savedNumber = [allDraws[countForCycles][0], allDraws[countForCycles][4],
                                   countForCycles]
            countForCycles = countForCycles + 1

        #print(savedNumber)
        return savedNumber[2], allDraws, numberOpponents, highOrLow

    else: #low card
        savedNumber = [1000, 1000, 1000]  # number of card, bonus value, position
        for x in allDraws:
            #print(countForCycles)
            # print(allDraws[countForCycles])
            # print(allDraws[countForCycles][0])

            if (allDraws[countForCycles][2] == True):  # calhou joker
                print(allDraws[countForCycles])
                return countForCycles, allDraws, numberOpponents, highOrLow

            if (savedNumber[0] > allDraws[countForCycles][0]):
                savedNumber = [allDraws[countForCycles][0], allDraws[countForCycles][4], countForCycles]
            if (savedNumber[0] == allDraws[countForCycles][0]):
                if (savedNumber[1] > allDraws[countForCycles][4]):
                    savedNumber = [allDraws[countForCycles][0], allDraws[countForCycles][4],
                                   countForCycles]  # number of card, bonus value, position

            countForCycles = countForCycles + 1

        print(savedNumber)
        return savedNumber[2], allDraws, numberOpponents, highOrLow

def drawCards(dificultyOp, jokerOp, currentCards):
    number = numc(dificultyOp)
    suit = suitc()

    for z in currentCards:
        if(z[0] == number and z[1] == suit):
            #draw again
            return drawCards(dificultyOp, jokerOp, currentCards)


    joker = j(jokerOp)
    win = joker
    bonus = bonusc()

    return number, suit, joker, win, bonus

#newGame(1,0,0,0)
