# 

from critter import *


class Wildcat(Critter):
    def __init__(self):
        super(Wildcat, self).__init__()

    def eat(self):
        return False

    def fight(self, opponent):
        incoming_attack = opponent.fight()
        if incoming_attack = 

    def get_color(self):
        return ""

    def get_move(self):
        return ""

    def __str__(self):
        return "&"
