#High/Low Card Generator
Requirements: Python 3.8,DJango latest version
IDE used: PyCharm
A Card based Luck game using Random variables
with options
Variable H: Option 0(default)-50/50 chance of the winner being the player with the highest/lowest
            Option 1-High Card Wins
            Option 2-Low Card Wins
Variable N: Option 0(default)- 1-3 Oponents(25% chance of 1 oponent 50% of 2 oponents and 25% of 3 oponents)
            Option 1- 1-2 Oponents(50/50 chance)
            Option 2- Exactly 1 Oponent
Variable D: Option 0(default)- returns a dificulty between 0,5 and 1 (easy dificulty)
            Option 1-returns a dificulty between 0,25 and 0,75 (medium dificulty)
            Option 2-returns a dificulty between 0 and 0,25 (hard dificulty)
Variable C: returns a suit and a value for the card (1-13 respectively A-K) and a bonus for tie breaking porpuse between 0-50
card ods are determined by (1/13)*(Variable D output) for each card and then the 5 middle cards(values 5-9) get the rest of the probaility density meaning each of the cards gets a total of  (1/13)*(Variable D output) + (1-(Variable D output))/5 for the human player and the odds are simply 1/13 for each card in the oponents draw.
Variable J: Option 0(default)- 1% chance of getting a "Joker" after the draw, the Joker is essentially a trump card and beats every other card regardless of Highest or Lowest                 beeing the winner
            Option 1-0.1% chance of getting the "Joker"after the draw
            Option 2-Joker of
The process is simple first variable H is instanciated to know which card wins then variable N is instanciated to know how many oponents subsequentialy Variable D is instanciated and then used in Variable C to get the human player´s card draw and bonus then the remaining oponents cards and bonuses are drawn, finally Variable J is instanciated for each player and the winner is decided concluding the game.
