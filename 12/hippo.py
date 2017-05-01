# This class represents a Stone type of Critter
# It changes direction after 5 moves, and only eats X amount
# of times during its life.
# it is represented by a gray S

from critter import *
from random import *


class Hippo(Critter):
    def __init__(self, hunger):
        super(Hippo, self).__init__()
        self.__hunger = hunger
        self.__move_count = 0
        self.__move_dir = 0

    def eat(self):
        if self.__hunger != 0:
            self.__hunger -= 1
            return True
        return False

    def fight(self, opponent):
        if self.__hunger > 0:
            return ATTACK_SCRATCH
        return ATTACK_POUNCE

    def get_color(self):
        if self.__hunger > 0:
            return "gray"
        return "white"

    def get_move(self):
        # If we've moved 5 times, time to go another way
        if self.__move_count > 5:
            self.__move_count = 0
        # If the move count is reset, generate a new number and direction
        if self.__move_count == 0:
            self.__move_dir = randint(1, 4)
        if self.__move_dir == 1:
            return DIRECTION_NORTH
        elif self.__move_dir == 2:
            return DIRECTION_EAST
        elif self.__move_dir == 3:
            return DIRECTION_SOUTH
        elif self.__move_dir == 4:
            return DIRECTION_WEST
        self.__move_count += 1

    def __str__(self):
        return str(self.__hunger)
