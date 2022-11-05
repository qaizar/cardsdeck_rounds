from cardRounds.calCardRounds import cardsDeck
import re
import os
import pytest

class TestCardsRoundsClass:
    
    input_deck_size = 7
    testCardDeck = cardsDeck()

    def test_setOriginalDeck(self):
        expectedDeck = [0, 1, 2, 3, 4, 5, 6]
        actualDeck = self.testCardDeck.setOriginalDeck(self.input_deck_size)
        assert self.testCardDeck.setOriginalDeck(self.input_deck_size)
        assert expectedDeck == actualDeck
    
    #***********************************
    # Testing with input_deck_size = 10
    #***********************************
    def test_setOriginalDeck_ten(self):
        expectedDeck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        actualDeck = self.testCardDeck.setOriginalDeck(10)
        assert self.testCardDeck.setOriginalDeck(self.input_deck_size)
        assert expectedDeck == actualDeck

    @pytest.mark.xfail(reason="Invalid input card value")
    def test_setOriginalDeck_Invalid(self):
        input_size = "a"
        with pytest.raises(TypeError):
            self.testCardDeck.setOriginalDeck(input_size)

    def test_tableRound(self):
        original_deck = self.testCardDeck.setOriginalDeck(self.input_deck_size)
        expectedTableDeck = [5, 1, 3, 6, 4, 2, 0]
        actualTableDeck = self.testCardDeck.tableRound()
        assert self.testCardDeck.tableRound()
        assert expectedTableDeck == actualTableDeck

    #***********************************
    # Testing with input_deck_size = 10
    #***********************************
    def test_tableRound_ten(self):
        original_deck = self.testCardDeck.setOriginalDeck(10)
        expectedTableDeck = [3, 7, 9, 5, 1, 8, 6, 4, 2, 0] 
        actualTableDeck = self.testCardDeck.tableRound()
        assert self.testCardDeck.tableRound()
        assert expectedTableDeck == actualTableDeck      

    def test_resetToOriginal(self):
        original_deck = self.testCardDeck.setOriginalDeck(self.input_deck_size)
        initial_tableround_deck = self.testCardDeck.tableRound()
        expectedNumRounds =  [5, 1, 5, 5, 1, 5, 5]
        actualNumRounds = self.testCardDeck.resetToOriginal(initial_tableround_deck)        
        assert self.testCardDeck.resetToOriginal(initial_tableround_deck)
        assert expectedNumRounds == actualNumRounds

    #***********************************
    # Testing with input_deck_size = 10
    #***********************************
    def test_resetToOriginal_ten(self):
        original_deck = self.testCardDeck.setOriginalDeck(10)
        initial_tableround_deck = [3, 7, 9, 5, 1, 8, 6, 4, 2, 0]
        expectedNumRounds =  [6, 3, 6, 6, 3, 6, 1, 3, 6, 6]
        actualNumRounds = self.testCardDeck.resetToOriginal(initial_tableround_deck)        
        assert self.testCardDeck.resetToOriginal(initial_tableround_deck)
        assert expectedNumRounds == actualNumRounds        

    def test_totalRounds(self):
        original_deck = self.testCardDeck.setOriginalDeck(self.input_deck_size)
        initial_tableround_deck = self.testCardDeck.tableRound()
        numRoundsForEachCard = self.testCardDeck.resetToOriginal(initial_tableround_deck)
        expectedNumRounds =  5
        actualNumRounds = self.testCardDeck.totalRounds(numRoundsForEachCard)
        assert self.testCardDeck.totalRounds(numRoundsForEachCard)
        assert expectedNumRounds == actualNumRounds

    #***********************************
    # Testing with input_deck_size = 10
    #***********************************
    def test_totalRounds_ten(self):
        original_deck = self.testCardDeck.setOriginalDeck(10)
        numRoundsForEachCard = [6, 3, 6, 6, 3, 6, 1, 3, 6, 6]
        expectedNumRounds =  6
        actualNumRounds = self.testCardDeck.totalRounds(numRoundsForEachCard)
        assert self.testCardDeck.totalRounds(numRoundsForEachCard)
        assert expectedNumRounds == actualNumRounds

    
    def test_roundsToOrgDeck(self):
        original_deck = self.testCardDeck.setOriginalDeck(self.input_deck_size)
        tablRound = self.testCardDeck.tableRound()
        resetToOrg = self.testCardDeck.resetToOriginal(tablRound)
        totalRnds = self.testCardDeck.totalRounds(resetToOrg)
        expectedTotalRounds = 5
        actualTotalRounds = totalRnds
        assert expectedTotalRounds == actualTotalRounds

    #***********************************
    # Testing with input_deck_size = 10
    #***********************************
    def test_roundsToOrgDeck_ten(self):
        original_deck = self.testCardDeck.setOriginalDeck(10)
        tablRound = [3, 7, 9, 5, 1, 8, 6, 4, 2, 0]
        resetToOrg = self.testCardDeck.resetToOriginal(tablRound)
        totalRnds = self.testCardDeck.totalRounds(resetToOrg)        
        expectedTotalRounds = 6
        actualTotalRounds = totalRnds
        assert expectedTotalRounds == actualTotalRounds


#*************************************
# Other "input_deck_size" with results
# *************************************
# 25 cards will take => 63 rounds
# 26 cards will take => 26 rounds
# 27 cards will take => 27 rounds
# 28 cards will take => 18 rounds
# 29 cards will take => 66 rounds
# 30 cards will take => 12 rounds

# 46 cards will take => 30 rounds
# 47 cards will take => 60 rounds
# 48 cards will take => 48 rounds
# 49 cards will take => 120 rounds
# 50 cards will take => 50 rounds
# 51 cards will take => 42 rounds
# 52 cards will take => 510 rounds