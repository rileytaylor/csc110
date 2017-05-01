# A Wildcat. Yay.
# It's represented by a cyan &.

from critter import *
from random import *

directions = DIRECTION_EAST, DIRECTION_WEST, DIRECTION_SOUTH, DIRECTION_NORTH

class Wildcat(Critter):
    def __init__(self):
        super(Wildcat, self).__init__()
        self.__other_cat = ''
        self.__last_attack = None
        self.__other_cats_bane = []

    def eat(self):
        neighbor = False
        for d in directions:
            if self.get_neighbor(directions[d]) != " ":
                neighor = True
        if neighbor:
            return False
        return True

    def fight(self, opponent):
        #Switch?
        if opponent == "%":
            return ATTACK_ROAR
        elif opponent == "S":
            return ATTACK_POUNCE
        elif opponent == "^" or "<" or ">" or "V":
            return ATTACK_SCRATCH
        elif int(opponent) == 1 or 2 or 3 or 4 or 5:
            return ATTACK_ROAR
        elif int(opponent) == 0:
            return ATTACK_SCRATCH
        # Best chance against the Aardvark
        elif opponent == "a" or "A":
            return ATTACK_POUNCE
        # A little something special for the other cat. Meow.
        elif opponent == self.__other_cat:
            #return self.__other_cats_bane
            #return the most common item
        # There's a new kid in town....
        else:
            self.__other_cat = opponent
            self.__last_attack = ATTACK_SCRATCH
            return ATTACK_SCRATCH

    def get_color(self):
        return "cyan"

    def get_move(self):
        # just move to the first empty space, this wildcats a loner
        move = False
        for d in directions:
            if self.get_neighbor(directions[d]) == " ":
                move = True
                return directions[d]
        if not move:
            return directions[randint(0, 3)]

    def __str__(self):
        return "&"

    def win(self):
        print("¯\_(ツ)_/¯")
        if self.__other_cat != '':
            self.__other_cats_bane.append(self.__last_attack)
        print("Take that " + self.__other_cat)

    def mate(self):
        print("Oh, my!")

    def lose(self):
        print("Suprise! I'm a Rakshasa, and I'm comin' back for you!")
        # Oh but i wish... but still, I'm gonna tell my buddies about you
