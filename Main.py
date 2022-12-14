import random, Objects

suitKey = ["Hearts", "Diamonds", "Spades", "Clubs"]
numberKey = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
players = []
cardsDealt = []
river = []

def main():
    print("Welcome to PokerSim!")
    addPlayers()
    deal()
    threeTurned()
    printRiver()
    oneTurned()
    printRiver()
    oneTurned()
    printRiver()

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
        players.append(Objects.Player(i, newName))
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

def threeTurned():
    i = 0
    while i < 3:
        river.append(str(randomCardGenerator()))
        i += 1

def oneTurned():
    river.append(str(randomCardGenerator()))

def printRiver():
    print(", ".join(river))




if __name__ == "__main__":
    main()