# A Wildcat. Yay.
# It's represented by a cyan &.
# I wanted to build in a learning mechanism for dealing with the other
# wildcat, but the time required without using 3rd-party libraries turned
# out to be not worth it. Oh well, it still cleans house of the other types.

from critter import *
from random import randint

directions = DIRECTION_EAST, DIRECTION_WEST, DIRECTION_SOUTH, DIRECTION_NORTH
attacks = ATTACK_POUNCE, ATTACK_SCRATCH, ATTACK_ROAR

class Wildcat(Critter):
    def __init__(self):
        super(Wildcat, self).__init__()

    def eat(self):
        neighbor = False
        for d in directions:
            if self.get_neighbor(directions[d]) != " ":
                neighor = True
        if neighbor:
            return False
        return True

    def fight(self, opponent):
        self.cat_was_last_opponent = False
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
        elif opponent == "a" or "A":
            # Best chance against the Aardvark
            return ATTACK_POUNCE
        else:
            r = randint(0,2)
            return attacks[r]

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
