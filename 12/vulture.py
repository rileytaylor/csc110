# This class represents a Stone type of Critter
# It stays still, doesn't eat and roars for an attack
# it is represented by a gray S

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
