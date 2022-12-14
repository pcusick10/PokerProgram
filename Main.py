import random, Objects

suitKey = ["Hearts", "Diamonds", "Spades", "Clubs"]
numberKey = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
players = []
cardsDealt = []

def main():
    print("Welcome to PokerSim!")
    addPlayers()
    deal()
    r = Objects.River()
    r.threeTurned()
    print(r)
    r.oneTurned()
    print(r)
    r.oneTurned()
    print(r)
    return 0

def randomCardGenerator():
    suit = randomSuit()
    number = randomNumber()
    if cardExists(number, suit):
        return randomCardGenerator()
    else:
        x = Objects.Card(suit, number)
        cardsDealt.append(x)
        return x
        

def randomSuit():
    return suitKey[random.randint(0, 3)]

def randomNumber():
    return numberKey[random.randint(0, 12)]

def addPlayers():
    x = int(input("Type the number of players you would like and press enter: "))
    if (x <= 0) or (x > 9):
        print("You can't play with that number of players, no more than nine players are allowed, try again.")
        addPlayers()
    i = 1
    while i <= x:
        newName = input("What would you like the name of Player " + str(i) + " to be: ")
        players.append(Objects.Player(i, newName))
        i += 1


def cardExists(num, suit):
    if cardsDealt:
        for c in cardsDealt:
            if (c.number == num) and (c.suit == suit):
                return True
        return False
    return False

def deal():
    for p in players:
        x = randomCardGenerator()
        y = randomCardGenerator()
        cardsDealt.append(x)
        cardsDealt.append(y)
        p.dealt(randomCardGenerator(), randomCardGenerator())
    for p in players:
        p.printHand()




if __name__ == "__main__":
    main()