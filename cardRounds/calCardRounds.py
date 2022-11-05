#!/usr/bin/env python3

import sys
from math import gcd
from functools import reduce
from copy import deepcopy

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class cardsDeck:
    def __init__(self):
        self.original_deck = None

    # set card deck based on input of cards
    def setOriginalDeck(self, original_deck):
        original_deck = original_deck

        if not str(original_deck).isdigit():
            print(f"{bcolors.FAIL}\nInvalid input for cards '{original_deck}'\n{bcolors.ENDC}")
            sys.exit(1)

        self.original_deck = list(range(0, original_deck))
        return self.original_deck

    # deck after step 1 to 3 - one table round
    def tableRound(self):
        startDeck = deepcopy(self.original_deck)
        initial_tableround_deck = []
        while len(startDeck) > 0:
            initial_tableround_deck.insert(0, startDeck.pop(0))        
            if len(startDeck) != 0:
                startDeck.append(startDeck.pop(0))
        return initial_tableround_deck

    # step 4 - reset deck to original order
    # Capture number of rounds it takes for each card to reset to original
    def resetToOriginal(self, initial_tableround_deck):
        numRoundsForEachCard = [1] * len(initial_tableround_deck)
        for card in (self.original_deck):
            index = card
            while initial_tableround_deck[index] != card:
                index = initial_tableround_deck[index]
                numRoundsForEachCard[card] += 1
        return numRoundsForEachCard
        
    # Finally the lowest common multiple of the number of rounds 
    # for each card will give the total rounds
    def totalRounds(self, numRoundsForEachCard):
        #e.g.: reduce(lambda a,b: a*b, [1, 2, 3, 4, 5]) calculates ((((1*2)*3)*4)*5)
        lcm = reduce(lambda a,b: a*b // gcd(a,b), numRoundsForEachCard)
        return lcm

    # Number of rounds to original deck
    def roundsToOrgDeck(self):
        tablRound = self.tableRound()
        resetToOrg = self.resetToOriginal(tablRound)
        totalRnds = self.totalRounds(resetToOrg)
        return totalRnds

if __name__ == "__main__":
    if (len(sys.argv) == 2) and (str(sys.argv[1]).isdigit() and int(sys.argv[1]) > 0):
        input_size = int(sys.argv[1])
        #input_size = 52
        cardsdeck = cardsDeck()
        cardsdeck.setOriginalDeck(input_size)
        roundsTotal = cardsdeck.roundsToOrgDeck()

        print(f"\n{bcolors.HEADER}------- Result: -------{bcolors.ENDC}\nDeck of {bcolors.OKYELLOW}{bcolors.BOLD}{input_size}{bcolors.ENDC} cards will take => "
              f"{bcolors.OKGREEN}{roundsTotal}{bcolors.ENDC} rounds to put the deck back into the original order\n"
              )
    else:
        print(f"{bcolors.FAIL}\nPlease run the command as below, arg must be valid number greater then 0:\n\n\t$ ./cards.py 10\n{bcolors.ENDC}")