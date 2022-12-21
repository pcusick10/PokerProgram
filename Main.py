import random, Objects
from queue import Queue

suitKey = ["Hearts", "Diamonds", "Spades", "Clubs"]
numberKey = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
players = []
cardsDealt = []
river = []
pot = 0
action = Queue(maxsize=9)
currentBet = -1
mostRecentBetter = ""
startingPlayer = 0


def main():
    global currentBet, mostRecentBetter, river, cardsDealt
    print("Welcome to PokerSim!")
    addPlayers()
    numPlayers = len(players)
    while(0 == 0):
        initQueue()
        deal()
        actionPrompt()
        if (action.qsize() != 1):
            mostRecentBetter = ""
            currentBet = -1
            flop()
            printRiver()
            actionPrompt()
            if (action.qsize() != 1):
                mostRecentBetter = ""
                currentBet = -1
                turnAndRiver()
                printRiver()
                actionPrompt()
                if (action.qsize() != 1):
                    mostRecentBetter = ""
                    currentBet = -1
                    turnAndRiver()
                    printRiver()
                    actionPrompt()
                else:
                    declareWinner(action.queue[0])
            else:
                declareWinner(action.queue[0])
        else:
            declareWinner(action.queue[0])
        declareWinner(checkCards(action))
        while(0 == 0):
            x = str(input("Are you done using PokerSim (y/n)? "))
            if x != "y" and x != "n":
                print("Please type \"y\" or \"n\"")
            else:
                break
        if x == "y":
            print("Thanks for playing!")
            break
    if startingPlayer == numPlayers - 1:
        startingPlayer = 0
    else:
        startingPlayer += 1
    river = []
    cardsDealt = []

def randomCardGenerator():
    x = Objects.Card(randomSuit(), randomNumber())
    if cardExists(x):
        #print(str(x) + " has already been dealt.")
        return randomCardGenerator()
    else:
        cardsDealt.append(x)
        #print(str(x) + " has been added to the cardsDealt array.")
        return x
        
def randomSuit():
    return suitKey[random.randint(0, 3)]

def randomNumber():
    return numberKey[random.randint(0, 12)]

def addPlayers():
    while 0 == 0:
        x = int(input("Type the number of players you would like and press enter: "))
        if (x > 0) and (x <= 9):
            break
        print("You can't play with that number of players, no more than nine players are allowed, try again.")
    i = 1
    while i <= x:
        newName = input("What would you like the name of Player " + str(i) + " to be: ")
        buyInAmount = int(input("How much is " + newName + " buying in? "))
        np = Objects.Player(i, newName, buyInAmount)
        players.append(np)
        action.put(np)
        i += 1

def cardExists(card):
    for c in cardsDealt:
        if (c == card):
            return True
    return False

def deal():
    for p in players:
        p.dealt(randomCardGenerator(), randomCardGenerator())
    for p in players:
        p.printHand()

def flop():
    i = 0
    while i < 3:
        river.append(randomCardGenerator())
        i += 1

def turnAndRiver():
    river.append(randomCardGenerator())

def printRiver():
    newRiver = []
    for c in river:
        newRiver.append(str(c))
    print(", ".join(newRiver))

def bet(player, amount):
    global pot
    #if player.stack < amount:
        #print("You don't have enough money to place this bet")
    print(player.playerName + " has bet " + str(amount))
    action.put(action.get())
    pot += amount
    player.stack -= amount

def rize(player, amount):
    global pot, mostRecentBetter, currentBet
    print(player.playerName + " has raised the bet to " + str(amount))
    mostRecentBetter = player.playerName
    currentBet = amount
    pot += amount
    player.stack -= amount
    action.put(action.get())

def fold(player):
    print(player.playerName + " has folded")
    action.get()

def check(player):
    global currentBet
    print(player.playerName + " has checked")
    action.put(action.get())
    currentBet = 0

def initQueue():
    sp = startingPlayer
    if sp == 0:
        for p in players:
            action.put(p)
    else:
        i = sp
        while i < len(players):
            action.put(players[i])
            i += 1
        i = 0
        while i < sp:
            action.put(players[i])
            i += 1

def actionPrompt():
    global currentPlayer, currentBet
    while(0 == 0):
        currentPlayer = action.queue[0]
        if not allGood(currentPlayer):
            print("Action is to " + currentPlayer.playerName)
            if (currentBet != -1) and (currentBet != 0):
                while 0 == 0:
                    x = str(input("Current bet is at " + str(currentBet) + ", choose to call, raise, or fold (c/r/f): "))
                    if (x != "c") and (x != "r") and (x != "f"):
                        print("Not a valid entry, please type \"c\" for call, \"r\" for raise, or \"f\" for fold.")
                    else:
                        break
                if x == "c":
                    bet(currentPlayer, currentBet)
                if x == "r":
                    r = int(input("How much would you like to raise the current bet by? "))
                    rize(currentPlayer, r + currentBet)
                if x == "f":
                    fold(currentPlayer)
            else:
                while 0 == 0:
                    x = str(input("No current bet, choose to check or raise (c/r): "))
                    if (x != "c") and (x != "r"):
                        print("Not a valid entry, please type \"c\" for check or \"r\" for raise")
                    else:
                        break
                if x == "c":
                    check(currentPlayer)
                if x == "r":
                    currentBet = 0
                    r = int(input("How much would you like to raise? "))
                    rize(currentPlayer, currentBet + r)
        else:
            break
   
def allGood(player):
    global startingPlayer
    if player.playerName == mostRecentBetter:
        return True
    elif (player == players[startingPlayer]) and (currentBet == 0):
        return True
    else:
        return False

def flush(player):
    hand = initHand(player)
    for s in suitKey:
        i = 0
        for c in hand:
            if(c.suit == s):
                i += 1
        if (i >= 5):
            return True
    return False
    
def pair(player):
    hand = initHand(player)
    for c in hand:
        for card in hand:
            if (c.number == card.number) and (c != card):
                return True
    return False

def twoPair(player):
    hand = initHand(player)
    pairs = []
    for c in hand:
        for card in hand:
            if (c.number == card.number) and (c != card) and (c.number not in pairs):
                pairs.append(c.number)
    if (len(pair) >= 2):
        return True
    return False

def threeOfaKind(player):
    hand = initHand(player)
    for c in hand:
        i = 1
        for card in hand:
            if (c.number == card.number) and (c != card):
                i += 1
        if (i >= 3):
            return True
    return False

def fourOfAKind(player):
    hand = initHand(player)
    for c in hand:
        i = 1
        for card in hand:
            if (c.number == card.number) and (c != card):
                i += 1
        if (i >= 4):
            return True
    return False

def fullHouse(player):
    hand = initHand(player)
    cardCount = {i : hand.count(i) for i in numberKey}
    pairs = 0
    trips = 0
    for c in cardCount:
        if cardCount[c] == 2:
            pair += 1
        elif cardCount[c] == 3:
            trips += 1
    if (trips >= 1) and (pairs >= 1):
        return True
    return False

def straight(player):
    hand = sortCards(initHand(player))
    mostInARow = 0
    cardsInARow = 0
    i = 0
    while i < len(hand):
        if (hand[i] == hand[i + 1] + 1):
            cardsInARow += 1
        else:
            cardsInARow = 0
        if cardsInARow == 5:
            return True
        i += 1
    return False

def initHand(player):
    hand = river
    for c in player.cards:
        hand.append(c)
    return hand

def sortCards(hand):
    #Returns a list of ints representing the index of the original card value in descending order, helps with determining if the hand has a straight
    cardKeys = []
    for c in hand:
        cardKeys.append(numberKey.index(c.number))
    sorted = []
    i = 0
    size = len(cardKeys)
    while i < size:
        max = max(cardKeys)
        sorted.append(max)
        cardKeys.remove(max)
        i += 1
    return sorted

def max(hand):
    max = 0
    for c in hand:
        if c > max:
            max = c
    return max
    
def checkCards(action):
    for p in action:
        if fourOfAKind(p):
            p.setHandRank(7)
        elif fullHouse(p):
            p.setHandRank(6)
        elif flush(p):
            p.setHandRank(5)
        elif straight(p):
            p.setHandRank(4)
        elif threeOfaKind(p):
            p.setHandRank(3)
        elif twoPair(p):
            p.setHandRank(2)
        elif pair(p):
            p.setHandRank(1)
    ranks = []
    for p in players:
        ranks.append(p.getHandRank())
    return players[ranks.index(max)]


def declareWinner(player):
    print(player.playerName + " has won " + str(pot) + "!")
    player.stack += pot

if __name__ == "__main__":
    main()