from django.shortcuts import render
from .models import *
from .game import *


def gameCard(suit, number):
    if(suit == "Hearts"):
        if(number == 1):
            return "../../static/applicationHLCG/media/1H.jpg"
        if (number == 2):
            return "../../static/applicationHLCG/media/2H.jpg"
        if (number == 3):
            return "../../static/applicationHLCG/media/3H.jpg"
        if (number == 4):
            return "../../static/applicationHLCG/media/4H.jpg"
        if (number == 5):
            return "../../static/applicationHLCG/media/5H.jpg"
        if (number == 6):
            return "../../static/applicationHLCG/media/6H.jpg"
        if (number == 7):
            return "../../static/applicationHLCG/media/7H.jpg"
        if (number == 8):
            return "../../static/applicationHLCG/media/8H.jpg"
        if (number == 9):
            return "../../static/applicationHLCG/media/9H.jpg"
        if (number == 10):
            return "../../static/applicationHLCG/media/10H.jpg"
        if (number == 11):
            return "../../static/applicationHLCG/media/11H.jpg"
        if (number == 12):
            return "../../static/applicationHLCG/media/12H.jpg"
        if (number == 13):
            return "../../static/applicationHLCG/media/13H.jpg"

    if (suit == "Clubs"):
        if (number == 1):
            return "../../static/applicationHLCG/media/1C.jpg"
        if (number == 2):
            return "../../static/applicationHLCG/media/2C.jpg"
        if (number == 3):
            return "../../static/applicationHLCG/media/3C.jpg"
        if (number == 4):
            return "../../static/applicationHLCG/media/4C.jpg"
        if (number == 5):
            return "../../static/applicationHLCG/media/5C.jpg"
        if (number == 6):
            return "../../static/applicationHLCG/media/6C.jpg"
        if (number == 7):
            return "../../static/applicationHLCG/media/7C.jpg"
        if (number == 8):
            return "../../static/applicationHLCG/media/8C.jpg"
        if (number == 9):
            return "../../static/applicationHLCG/media/9C.jpg"
        if (number == 10):
            return "../../static/applicationHLCG/media/10C.jpg"
        if (number == 11):
            return "../../static/applicationHLCG/media/11C.jpg"
        if (number == 12):
            return "../../static/applicationHLCG/media/12C.jpg"
        if (number == 13):
            return "../../static/applicationHLCG/media/13C.jpg"

    if (suit == "Diamonds"):
        if (number == 1):
            return "../../static/applicationHLCG/media/1D.jpg"
        if (number == 2):
            return "../../static/applicationHLCG/media/2D.jpg"
        if (number == 3):
            return "../../static/applicationHLCG/media/3D.jpg"
        if (number == 4):
            return "../../static/applicationHLCG/media/4D.jpg"
        if (number == 5):
            return "../../static/applicationHLCG/media/5D.jpg"
        if (number == 6):
            return "../../static/applicationHLCG/media/6D.jpg"
        if (number == 7):
            return "../../static/applicationHLCG/media/7D.jpg"
        if (number == 8):
            return "../../static/applicationHLCG/media/8D.jpg"
        if (number == 9):
            return "../../static/applicationHLCG/media/9D.jpg"
        if (number == 10):
            return "../../static/applicationHLCG/media/10D.jpg"
        if (number == 11):
            return "../../static/applicationHLCG/media/11D.jpg"
        if (number == 12):
            return "../../static/applicationHLCG/media/12D.jpg"
        if (number == 13):
            return "../../static/applicationHLCG/media/13D.jpg"

    if (suit == "Spades"):
        if (number == 1):
            return "../../static/applicationHLCG/media/1S.jpg"
        if (number == 2):
            return "../../static/applicationHLCG/media/2S.jpg"
        if (number == 3):
            return "../../static/applicationHLCG/media/3S.jpg"
        if (number == 4):
            return "../../static/applicationHLCG/media/4S.jpg"
        if (number == 5):
            return "../../static/applicationHLCG/media/5S.jpg"
        if (number == 6):
            return "../../static/applicationHLCG/media/6S.jpg"
        if (number == 7):
            return "../../static/applicationHLCG/media/7S.jpg"
        if (number == 8):
            return "../../static/applicationHLCG/media/8S.jpg"
        if (number == 9):
            return "../../static/applicationHLCG/media/9S.jpg"
        if (number == 10):
            return "../../static/applicationHLCG/media/10S.jpg"
        if (number == 11):
            return "../../static/applicationHLCG/media/11S.jpg"
        if (number == 12):
            return "../../static/applicationHLCG/media/12S.jpg"
        if (number == 13):
            return "../../static/applicationHLCG/media/13S.jpg"



def game(request):
    aux = GameSettings.objects.last()

    hlOption = aux.hlOption
    numPlayersOption = aux.numPlayersOption
    dificultyOp = aux.dificultyOp
    jokerOp = aux.jokerOp

    allResults = newGame(hlOption, numPlayersOption, dificultyOp, jokerOp)

    winner = allResults[0]
    allDraws = allResults[1]
    numberOpponents = allResults[2]
    highOrLow = allResults[3]


    if (winner == 0):
        message = "Ganhaste!!!!"
    if (winner == 1):
        message = "O oponente 1 ganhou."
    if (winner == 2):
        message = "O oponente 2 ganhou."
    if (winner == 3):
        message = "O oponente 3 ganhou."

    humanPlayerDraw = allDraws[0]
    humanCard = gameCard(humanPlayerDraw[1], humanPlayerDraw[0])
    valueBonusHuman = humanPlayerDraw[4]
    hJoker = jokerMesage(humanPlayerDraw[2])

    op1Draw = allDraws[1]
    op1Card = gameCard(op1Draw[1], op1Draw[0])
    valueBonusOp1 = op1Draw[4]
    op1Joker = jokerMesage(op1Draw[2])

    if (numberOpponents == 2 or numberOpponents == 3):
        op2Draw = allDraws[2]
        op2Card = gameCard(op2Draw[1], op2Draw[0])
        valueBonusOp2 = op2Draw[4]
        op2Joker = jokerMesage(op2Draw[2])

    if (numberOpponents == 3):
        op3Draw = allDraws[3]
        op3Card = gameCard(op3Draw[1], op3Draw[0])
        valueBonusOp3 = op3Draw[4]
        op3Joker = jokerMesage(op3Draw[2])

    if (numberOpponents == 1):
        context = {'cardPlayer': humanCard,
                   'valueBonusPlayer': valueBonusHuman,
                   'cardOp1': op1Card,
                   'valueBonusOp1': valueBonusOp1, 'winnerMessage': message, 'highOrLow': highOrLow, 'hJoker': hJoker, 'op1Joker': op1Joker

                   }
    if (numberOpponents == 2):
        context = {'cardPlayer': humanCard,
                   'valueBonusPlayer': valueBonusHuman,
                   'cardOp1': op1Card,
                   'valueBonusOp1': valueBonusOp1,
                   'cardOp2': op2Card,
                   'valueBonusOp2': valueBonusOp2,
                   'winnerMessage': message, 'highOrLow': highOrLow, 'hJoker': hJoker, 'op1Joker': op1Joker, 'op2Joker': op2Joker
                   }

    if (numberOpponents == 3):
        context = {'cardPlayer': humanCard,
                   'valueBonusPlayer': valueBonusHuman,
                   'cardOp1': op1Card,
                   'valueBonusOp1': valueBonusOp1,
                   'cardOp2': op2Card,
                   'valueBonusOp2': valueBonusOp2,
                   'cardOp3': op3Card,
                   'valueBonusOp3': valueBonusOp3,
                   'winnerMessage': message, 'highOrLow': highOrLow, 'hJoker': hJoker, 'op1Joker': op1Joker, 'op2Joker': op2Joker, 'op3Joker': op3Joker
                   }

    return render(request, 'website/game.html', context)

def jokerMesage(bool):
    if (bool == True):
        return "Joker"
    else:
        return ""


def settings(request):

    if request.method == 'POST':

        hlOption = request.POST['hlOption']
        numPlayersOption = request.POST['numPlayersOption']
        dificultyOp = request.POST['dificultyOp']
        jokerOp = request.POST['jokerOp']

        new_settings = GameSettings(hlOption=hlOption, numPlayersOption=numPlayersOption, dificultyOp=dificultyOp,
                                    jokerOp=jokerOp)
        new_settings.save()



    return render(request, 'website/settings.html')
