#
# Header
#

# TODO: Headers, haiku, fix pylint on this fucking mac

from random import *

MAX_NUMBER = 100


def main():
    again = True
    games = 0
    total_guesses = 0
    best_guesses = 0
    best_game = 0

    intro()

    # Prompt to play again here
    while (again == True):
        games += 1
        guesses = game()
        total_guesses += guesses
        if (guesses < best_guesses or best_game == 0):
            best_guesses = guesses
            best_game = games
        again = play_again()

    total(games, total_guesses, best_game)

def intro():
    print("Insert Haiku Here.")
    print()

def play_again():
    prompt = input("Do you want to play again? ")
    p = prompt.lower()
    if (p.startswith("y")):
        return True
    else:
        return False
    print()

def game():
    print("I'm thinking of a number between 1 and " + str(MAX_NUMBER) + "...")
    number = randint(1, MAX_NUMBER)
    guess = 0
    count = 0
    while (int(guess) != number):
        guess = input("Your Guess? ")
        if (int(guess) < number):
            print("It's higher.")
        elif (int(guess) > number):
            print("It's lower.")
        count += 1
    if (count > 1):
        print("You got it right in " + str(count) + " guesses!")
    else:
        print("You got it right in 1 guess!")
    return count

def total(games, guesses, best):
    guesses_per_game = guesses / games
    print("Overall results:")
    print("Total games   = " + str(games))
    print("Total guesses = " + str(guesses))
    print("Guesses/game  = " + str(guesses_per_game))
    print("Best game     = " + str(best))

main()