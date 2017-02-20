#
# Header
#

from random import *

MAX_NUMBER = 100


def main():
    games = 0
    total_count = 0
    best_game = 0

    intro()

    # Prompt to play again here
    if (games > 0):
        again = play_again()
        while (again == True):
            game()
    else:
        game()

    total()

def intro():
    print("Insert Haiku Here.")

def play_again():
    prompt = input("Do you want to play again? ")
    p = prompt.lower()
    if (p.startswith("y")):
        return True
    else:
        return False

def game():
    print("I'm thinking of a number between 1 and " + str(MAX_NUMBER) + "...")
    number = randint(1, MAX_NUMBER)
    guess = 0
    count = 0
    while (guess != number):
        guess = input("Your Guess? ")
        if (guess < number):
            print("It's higher.")
        elif (guess > number):
            print("It's lower.")
        count += 1
    if (count > 1):
        print("You got it right in " + str(guess) + " guesses!")
    else:
        print("You got it right in 1 guess!")
    games += 1
    total_count += count
    if (count < total_count):
        best_game = total_count

def total():
    guesses_per_game = total_count / games
    print("Overall results:")
    print("Total games   = " + str(games))
    print("Total guesses = " + str(total_count))
    print("Guesses/game  = " + str(guesses_per_game))
    print("Best game     = " + str(best_game))
