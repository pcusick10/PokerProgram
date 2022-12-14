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
    
    def __eq__(self, other) -> bool:
        return (self.suit == other.suit) and (self.number == other.number)
