import Main

class Player:

    def __init__(self, num, name):
        self.playerName = name
        self.playerNum = num
        self.cards = []
    
    def dealt(self, cardone, cardtwo):
        self.cards.append(cardone)
        self.cards.append(cardtwo)
    
    def printHand(self):
        print(self.playerName + "'s hand is the " + str(self.cards[0]) + " and the " + str(self.cards[1]))

class Card:

    def __init__(self, s, n):
        self.suit = s
        self.number = n
    
    def __str__(self):
        return self.number + " of " + self.suit

class River:

    def __init__(self):
        self.cards = []
    
    def __str__(self):
        return ", ".join(self.cards)
    
    def threeTurned(self):
        i = 0
        while i < 3:
            self.cards.append(Main.randomCardGenerator().__str__())
            i += 1
    
    def oneTurned(self):
        self.cards.append(Main.randomCardGenerator().__str__())