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
        mostRecentBetter = ""
        currentBet = -1
        flop()
        printRiver()
        actionPrompt()
        mostRecentBetter = ""
        currentBet = -1
        turnAndRiver()
        printRiver()
        actionPrompt()
        mostRecentBetter = ""
        currentBet = -1
        turnAndRiver()
        printRiver()
        actionPrompt()
        #declareWinner()
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

if __name__ == "__main__":
    main()