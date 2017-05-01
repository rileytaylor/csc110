# This class represents a Vulture type of Critter
# This is a bird that is only hungry after fighting.
# it is represented by a black arrow.

from bird import *


class Vulture(Bird):
    def __init__(self):
        super(Vulture, self).__init__()
        self.__hungry = True

    def eat(self):
        hunger = self.__hungry
        if self.__hungry:
            self.__hungry = False
        return hunger

    def fight(self, opponent):
        self.__hungry = True
        return super(Vulture, self).fight(opponent)

    def get_color(self):
        return "black"
