# WHERE THE RANDOM VARIABLE FUNCTIONS WILL BE STORED
from random import random

def h(option): #Function that decides if winner is the player with the highest/lowest card returns "High Card" if high card wins or "Low Card" if low card wins
    if option == 1: #Only High card wins
        return "High Card"
    elif option == 2: #Only Low card wins
        return "Low Card"
    elif option == 0: #Default random 50/50 high/low card wins
        random_variable_instance: float = random()
        if 0.5 < random_variable_instance and 1 >= random_variable_instance: #Guarantees a 50/50 chance of the winner being the player with the highest/lowest card
            return "High Card"
        else:
            return "Low Card"
    else:
        print("Invalid Option")
def j(option): #Function that decides weather a player got the joker wildcard returns true if the player got the joker or false if they didn't
    if option == 1: #0.1% chance of getting the joker
        random_variable_instance: float = random()
        if 0.999 < random_variable_instance and 1 >= random_variable_instance :  #Guarantees the 0.q% chance of getting the joker
            return True
        else:
            return False
    elif option == 2: #Joker off
            return False #Guarantees a 0% chance of getting the Joker
    elif option == 0: #Default 1% chance of getting the Joker
        random_variable_instance: float = random()
        if 0.99 < random_variable_instance and 1 >= random_variable_instance: #Guarantees a 1% chance of getting the Joker
            return True
        else:
            return False
    else:
        print("Invalid Option")

def n(option): #returns the number of computer players the user will play against 1,2 or 3
    if option == 1: #player wil ONLY play 1 opponent
        return 1
    elif option == 2: # Random 50/50 of playing 1 or 2 players
        random_variable_instance: float = random()
        if 0 < random_variable_instance and  0.5 >= random_variable_instance:
            return 1
        elif 1 >= random_variable_instance:
            return 2
    elif option == 0: #Default 25% chance of versing 1 player or 3 players and 50% chance of facing 2 players
        random_variable_instance: float = random()
        if 0 < random_variable_instance and 0.25 >= random_variable_instance: #Guarantees a 25% chance of playing against 1 player
            return 1
        elif 0.25 < random_variable_instance and 0.75 >= random_variable_instance: #Guarantees a 50% chance of playing 2 Players
            return 2
        elif 1 >= random_variable_instance: #Guarantees a 25% chance of playing 3 players
            return 3
    else:
        print("Invalid Option")

def d(option): #Returns the difficulty for the player
    if option == 1: # "medium" returns a number between 0.25 and 0.75
        return 0.5*random() +0.25
    elif option == 2: # "hard" returns a number between 0 and 0.25
        return 0.25*random()
    elif option == 0: #Default "easy" returns a number between 0.5 and 1
        return 0.5*random() +0.5
    else:
        print("Invalid Option")

def c(dif) -> str: #returns the "card" a number between 1 and 13 for the value (A to K) and the suit i.e (13,"Clubs") would be the King of clubs
    return numc(dif),suitc()

def numc(dif) -> int: #returns the value of the card
    random_variable_instance = random()
    if (0 < random_variable_instance and (1 * dif) / 13 >= random_variable_instance): # Ace with a probability of d/13
        return 1
    elif ((1 * dif) / 13 < random_variable_instance and (2 * dif) / 13 >= random_variable_instance): # 2 with a probability of d/13
        return 2
    elif ((2 * dif) / 13 < random_variable_instance and (3 * dif) / 13 >= random_variable_instance): # 3 with a probability of d/13
        return 3
    elif ((3 * dif) / 13 < random_variable_instance and (4 * dif) / 13 >= random_variable_instance): # 4 with a probability of d/13
        return 4
    elif (((4 * dif) / 13 < random_variable_instance and (5 * dif) / 13 >= random_variable_instance) or (dif < random_variable_instance and dif + ((1 - dif) / 5) >= random_variable_instance)): # 5 with a probability of d/13 + (1-d)/5
        return 5
    elif (((5 * dif) / 13 < random_variable_instance and (6 * dif) / 13 >= random_variable_instance) or (dif + ((1 - dif) / 5) < random_variable_instance and dif + ((2 * (1 - dif)) / 5) >= random_variable_instance)): # 6 with a probability of d/13 + (1-d)/5
        return 6
    elif (((6 * dif) / 13 < random_variable_instance and (7 * dif) / 13 >= random_variable_instance) or (dif + ((2 * (1 - dif)) / 5) < random_variable_instance and dif + ((3 * (1 - dif)) / 5) >= random_variable_instance)): # 7 with a probability of d/13 + (1-d)/5
        return 7
    elif (((7 * dif) / 13 < random_variable_instance and (8 * dif) / 13 >= random_variable_instance) or (dif + ((3 * (1 - dif)) / 5) < random_variable_instance and dif + ((4 * (1 - dif)) / 5) >= random_variable_instance)): # 8 with a probability of d/13 + (1-d)/5
        return 8
    elif (((8 * dif) / 13 < random_variable_instance and (9 * dif) / 13 >= random_variable_instance) or (dif + ((4 * (1 - dif)) / 5) < random_variable_instance and 1 >= random_variable_instance)): # 9 with a probability of d/13 + (1-d)/5
        return 9
    elif ((9 * dif) / 13 < random_variable_instance and (10 * dif) / 13 >= random_variable_instance): # 10 with a probability of d/13
        return 10
    elif ((10 * dif) / 13 < random_variable_instance and (11 * dif) / 13 >= random_variable_instance): # Jack with a probability of d/13
        return 11
    elif ((11 * dif) / 13 < random_variable_instance and (12 * dif) / 13 >= random_variable_instance): # Queen with a probability of d/13
        return 12
    elif ((12 * dif) / 13 < random_variable_instance and (13 * dif) / 13 >= random_variable_instance): # King with a probability of d/13
        return 13
def suitc() -> str: #returns the suit of the card with a 25% chance for each suit
    random_variable_instance = random()
    if 0 < random_variable_instance and 0.25 >= random_variable_instance:
        return "Diamonds"
    elif 0.25 < random_variable_instance and 0.5 >= random_variable_instance:
        return "Clubs"
    elif 0.5 < random_variable_instance and 0.75 >= random_variable_instance:
        return "Hearts"
    elif 0.75 < random_variable_instance and 1 >= random_variable_instance:
        return "Spades"
x = 0
y = 10
while x < y:
    #print(h(0))
    #print(h(1))
    #print(h(2))
    #print(j(0))
    #print(j(1))
    #print(j(2))
    #print(n(0))
    #print(n(1))
    #print(n(2))
    #print(d(0))
    #print(d(1))
    #print(d(2))
    #print(c(1))
    print(c(0.5))
    x = x + 1
