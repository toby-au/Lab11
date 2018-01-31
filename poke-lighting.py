"""
Toby Au
CSC1 141
Lab 11: Pokemon: Lightning Round
Pokemon Card game: each player gets a random deck of 15 cards, select which strategy to use and returns the winners ID
"""

from array_heap import *
import random


class Pokemon(struct):
    """
    pokemon class with slots name, HP, and ATK
    """
    _slots = ((str, "name"), (int, "HP"), (int, "ATK"))


def copyCard(card):
    """
    returns a deep copy of the passed-in card
    :param card:
    :return:
    """
    return Pokemon(card.name, card.HP, card.ATK)


def createDeck(pokeDex, size):
    """
    - creates the deck using pokeDex, the list of pokemon objects, and keeps the size of the deck constant
    - returns deck of pokemon objects
    :param pokeDex:
    :param size:
    :return:
    """
    deck = []
    for i in range(0, size):
        num = random.randint(0, len(pokeDex))
        card = copyCard(pokeDex[num])
        deck.append(card)
    return deck


def printDeck(deck):
    """
    prints deck
    :param deck:
    :return:
    """
    print(deck)


def readDex(file):
    """
    takes a filename to read and returns a listing of pokemon
    :param file:
    :return:
    """
    pokedex = []
    for line in open(file):
        pokemon = line.strip().split()
        if pokemon[0] != "Pokemon":
            pokedex.append(Pokemon(pokemon[0], int(pokemon[1]), int(pokemon[2])))
    return pokedex


##############################
# comparators for 6 user selectable strageties
##############################
def minHP(pokemon1, pokemon2):
    """
    compares HP of the two pokemon objects and returns True if the first pokemon
    has less HP than the second pokemon else returns False
    :param pokemon1:
    :param pokemon2:
    :return:
    """
    return pokemon1.HP <= pokemon2.HP

def maxHP(pokemon1, pokemon2):
    """
    compares HP of the two pokemon objects and returns True if the first pokemon
    has greater HP than the second pokemon else returns False
    :param pokemon1:
    :param pokemon2:
    :return:
    """
    return pokemon1.HP >= pokemon2.HP

def minATK(pokemon1, pokemon2):
    """
    compares ATK of the two pokemon objects and returns True if the first pokemon
    has less ATK than the second pokemon else returns False
    :param pokemon1:
    :param pokemon2:
    :return:
    """
    return pokemon1.ATK <= pokemon2.ATK

def maxATK(pokemon1, pokemon2):
    """
    compares ATK of the two pokemon objects and returns True if the first pokemon
    has greater ATK than the second pokemon else returns False
    :param pokemon1:
    :param pokemon2:
    :return:
    """
    return pokemon1.ATK >= pokemon2.ATK

def minBoth(pokemon1, pokemon2):
    """
    compares HP and ATK of both pokemon objects and returns True if the first pokemon has a minimum of both
    else returns False
    :param pokemon1:
    :param pokemon2:
    :return:
    """
    return pokemon1.HP <= pokemon2.HP and pokemon1.ATK <= pokemon2.ATK

def maxBoth(pokemon1, pokemon2):
    """
    compares HP and ATK of both pokemon objects and returns True if the first pokemon has a maximum of both
    else returns False
    :param pokemon1:
    :param pokemon2:
    :return:
    """
    return pokemon1.HP >= pokemon2.HP and pokemon1.ATK >= pokemon2.ATK



def attributes(deck):
    """
    helper function that orders the deck in terms of attributes and returns the new deck
    :param deck:
    :return:
    """
    newdeck = []
    attribute = input("Enter the order attribute and direction: ")
    for i in range(0, len(deck)-1):
        if attribute == "A":
            if minHP(deck[i], deck[i + 1]):
                newdeck.append(deck[i])
            else:
                newdeck.append(deck[i + 1])

        if attribute == "B":
            if maxHP(deck[i], deck[i + 1]):
                newdeck.append(deck[i])
            else:
                newdeck.append(deck[i + 1])

        if attribute == "C":
            if minATK(deck[i], deck[i + 1]):
                newdeck.append(deck[i])
            else:
                newdeck.append(deck[i + 1])

        if attribute == "D":
            if maxATK(deck[i], deck[i + 1]):
                newdeck.append(deck[i])
            else:
                newdeck.append(deck[i + 1])

        if attribute == "E":
            if minBoth(deck[i], deck[i+1]):
                newdeck.append(deck[i])
            else:
                newdeck.append(deck[i + 1])

        if attribute == "F":
            if maxBoth(deck[i], deck[i+1]):
                newdeck.append(deck[i])
            else:
                newdeck.append(deck[i + 1])
    return newdeck


def playGame(deck1, deck2):
    """
    takes in two decks, and returns the player ID (integer) of the winner
    :param deck1:
    :param deck2:
    :return:
    """
    for i in range(0, len(deck1)):
        for j in range(0, len(deck2)):



            if deck1[i].HP and deck2[i].HP >= 0:
                print("Player 1 plays ", deck1[i].name)
                print("Player 2 plays ", deck2[j].name)
                print(deck1[i].name, "attacks", deck2[j].name, "for", deck1[i].ATK, "damage")
                deck2[j].HP = deck2[j].HP - deck1[i].ATK
                print(deck2[j].name, "attacks", deck1[i].name, "for", deck2[j].ATK, "damage")
                deck1[i].HP = deck1[i].HP - deck2[j].ATK

            if deck1[i].HP <= 0:
                print(deck1[i].name, " fainted")
                deck1.remove(deck1[i])
            else:
                print(deck2[j].name, " fainted")
                deck2.remove(deck2[j])
            return playGame(deck1, deck2)



    if len(deck1) == 0:
        print("Player 2 is the winner !")
    else:
        print("Player 1 is the winner !")


def main():
    """
    - The main function contains print statements that simulates the game and allows user interaction such as inputting file and
    strategies.
    - prints the deck of both players, contains 15 pokemon
    - using the new deck, players battle to become the winner, returns the winner ID which is player 1 or player 2
    :return:
    """
    print("Welcome to the Pokemon Lighting Tournament !")
    file = input("Enter the name of the file containing the Pokemon: ")
    readDex(file)
    deck1 = (createDeck(readDex(file), 16))
    deck2 = (createDeck(readDex(file), 16))

    print("Player 1 > Which strategy will your deck use?")
    print("A (Min HP),", "B (Max HP),", "C (Min ATK),", "D (Max ATK),", "E (Min Both),", "F (Max Both)")
    newdeck1 = attributes(deck1)
    print("Your deck contains: ")
    pokemon1 = []
    for i in range(0, len(newdeck1)):
        pokemon1.append(newdeck1[i].name)
    print(pokemon1)
    print("Player2 > Which strategy will your deck use?")
    print("A (Min HP),", "B (Max HP),", "C (Min ATK),", "D (Max ATK),", "E (Min Both),", "F (Max Both)")
    newdeck2 = attributes(deck2)
    print("Your deck contains: ")
    pokemon2 = []
    for j in range(0, len(newdeck2)):
        pokemon2.append(newdeck2[j].name)
    print(pokemon2)
    playGame(newdeck1, newdeck2)
main()