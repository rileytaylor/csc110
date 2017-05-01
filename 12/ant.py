# This class represents a Ant type of Critter
# it is represented by a red %

# HW 12 Hours spent: 5

from critter import *


class Ant(Critter):
    def __init__(self, walk_south):
        super(Ant, self).__init__()
        self.__walk_south = walk_south
        self.__moves = 0

    def eat(self):
        return True

    def fight(self, opponent):
        return ATTACK_SCRATCH

    def get_color(self):
        return "red"

    def get_move(self):
        self.__moves += 1
        if self.__walk_south:
            if self.__moves % 2 == 0:
                return DIRECTION_EAST
            else:
                return DIRECTION_SOUTH
        if not self.__walk_south:
            if self.__moves % 2 == 0:
                return DIRECTION_EAST
            else:
                return DIRECTION_NORTH

    def __str__(self):
        return "%"
