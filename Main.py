import random, Objects
from queue import Queue

suitKey = ["Hearts", "Diamonds", "Spades", "Clubs"]
numberKey = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
players = []
cardsDealt = []
river = []
pot = 0
action = Queue(maxsize=9)
currentBet = 0


def main():
    print("Welcome to PokerSim!")
    addPlayers()
    numPlayers = len(players)
    startingPlayer = 0
    while(0 == 0):
        initQueue(startingPlayer)
        while(0 == 0):
            deal()
            actionPrompt()
            flop()
            printRiver()
            actionPrompt()
            turnAndRiver()
            printRiver()
            actionPrompt()
            turnAndRiver()
            printRiver()
            actionPrompt()
    if startingPlayer == numPlayers - 1:
        startingPlayer = 0
    else:
        startingPlayer += 1

       
    

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
        buyInAmount = input("How much is " + newName + " buying in? ")
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
    #if player.stack < amount:
        #print("You don't have enough money to place this bet")
    print(player.name + " has bet " + str(amount))
    action.put(action.get())
    pot += amount
    player.stack -= amount

def fold(player):
    print(player.name + " has folded")
    action.get()

def check(player):
    print(player.name + " has checked")
    action.put(action.get())

def initQueue(sp):
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
    currentPlayer = action.queue[0]
    print("Action is to " + currentPlayer.playerName)
    if (currentBet != 0):
        while 0 == 0:
            x = str(input("Current bet is at " + str(currentBet) + ", choose to call, raise, or fold (c/r/f): "))
            if (x != "c") or (x != "r") or (x != "f"):
                print("Not a valid entry, please type \"c\" for call, \"r\" for raise, or \"f\" for fold.")
            else:
                break
        if x == "c":
            bet(currentPlayer, currentBet)
        if x == "r":
            r = input("How much would you like to raise the current bet by? ")
            bet(currentPlayer, r + currentBet)
        if x == "f":
            print(currentPlayer.name + " has folded")
            fold(currentPlayer)
    else:
        while 0 == 0:
            x = str(input("No current bet, choose to check or bet (c/b): "))
            if (x != "c") or (x != "b"):
                print("Not a valid entry, please type \"c\" for check or \"b\" for bet")
            else:
                break
        if x == "c":
            check(currentPlayer)
        if x == "b":
            b = input("How much would you like to bet? ")
            bet(currentPlayer, b)


if __name__ == "__main__":
    main()