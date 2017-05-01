# This class represents a Bird type of Critter
# It moves in a square, and really hates ants.
# it is represented by a blue arrow.

from critter import *


class Bird(Critter):
    def __init__(self):
        super(Bird, self).__init__()
        self.__moves = 0
        self.__last_move = 'N'

    def eat(self):
        return False

    def fight(self, opponent):
        if opponent == "%":
            return ATTACK_ROAR
        else:
            return ATTACK_POUNCE

    def get_color(self):
        return "blue"

    def get_move(self):
        self.__moves += 1
        if self.__moves > 12:
            self.__moves = 1
        if self.__moves <= 3:
            self.__last_move = "N"
            return DIRECTION_NORTH
        elif self.__moves <= 6:
            self.__last_move = "E"
            return DIRECTION_EAST
        elif self.__moves <= 9:
            self.__last_move = "S"
            return DIRECTION_SOUTH
        elif self.__moves <= 12:
            self.__last_move = "W"
            return DIRECTION_WEST

    def __str__(self):
        if self.__last_move == "N":
            return "^"
        elif self.__last_move == "E":
            return ">"
        elif self.__last_move == "S":
            return "V"
        elif self.__last_move == "W":
            return "<"
