# Minimain
# Use this program to help test your critters
# It will create one of each Critter and then call all of its
# methods 10 times each

from ant import *
from bird import *
from hippo import *
from vulture import *

def main():
    animals = [Ant(False), Bird(), Hippo(5), Vulture()]
    for animal in animals:
        print(type(animal))
        one_critter(animal)


# calls all of the passed in animals methods 10 times each
# and prints what they return
def one_critter(animal):
    for i in range(0, 10):
        print("eat:       " + str(animal.eat()))
        print("fight:     " + str(animal.fight("v")))
        print("get_color: " + animal.get_color())
        print("get_move:  " + str(animal.get_move()))
        print("__str__:   " + str(animal))

main()
