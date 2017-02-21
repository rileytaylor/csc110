# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: Guessing Game
#
# This plays a guessing game with the user. The game can be played
# many times and will report overall statistics at the end.

from random import *

MAX_NUMBER = 100


def main():
    again = True
    games = 0
    total_guesses = 0
    best_guesses = 0
    best_game = 0

    intro()

    # Play the game
    while (again == True):
        games += 1
        guesses = game()
        total_guesses += guesses
        if (guesses < best_guesses or best_game == 0):
            best_guesses = guesses
            best_game = games
        print()
        again = play_again()

    total(games, total_guesses, best_game)


# --------------------------------------------------------------------
# intro() simply provides the introductory haiku.
# --------------------------------------------------------------------
def intro():
    print("\nFlying piano \nWobbles hastily, pleasant \nObscene lame monks fret.")


# --------------------------------------------------------------------
# play_again() asks if the user wants to play another game.
# RETURN:     a bool
# --------------------------------------------------------------------
def play_again():
    prompt = input("Do you want to play again? ")
    p = prompt.lower()
    if (p.startswith("y")):
        return True
    else:
        return False


# --------------------------------------------------------------------
# game() is the guessing game.
# RETURN:     an int representing the number of guesses made
# --------------------------------------------------------------------
def game():
    print("\nI'm thinking of a number between 1 and " 
          + str(MAX_NUMBER) 
          + "...")
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


# --------------------------------------------------------------------
# total() takes in data and returns overall statistics from games
# played by the user.
# PARAMETERS: games -- an int. The number of games played.
#             guesses -- an int. The number of guesses made.
#             best -- an int. The id of the game played with the
#                     fewest guesses
# --------------------------------------------------------------------
def total(games, guesses, best):
    guesses_per_game = guesses / games
    print("\nOverall results:")
    print("Total games   = " + str(games))
    print("Total guesses = " + str(guesses))
    print("Guesses/game  = " + str(guesses_per_game))
    print("Best game     = " + str(best))
    print()

main()