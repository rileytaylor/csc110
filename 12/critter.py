# Preliminary version of the Critter class
# we will give you a different version for the homework

# Version 2.1

# Constants for attacks, directions
ATTACK_POUNCE    = 0
ATTACK_ROAR      = 1    
ATTACK_SCRATCH   = 2
ATTACK_FORFEIT   = 3
DIRECTION_NORTH  = 0
DIRECTION_SOUTH  = 1
DIRECTION_EAST   = 2
DIRECTION_WEST   = 3
DIRECTION_CENTER = 4

class Critter():

    # Methods students will be implementing

    def eat(self):
        return False

    def fight(self, opponent):
        return ATTACK_FORFEIT

    def get_color(self):
        return "grey"

    def get_move(self):
        # print("here")
        return DIRECTION_CENTER

    def __str__(self):
        return "?"

    # End methods students will be implementing
    

    def __init__(self):
        self.x = -1
        self.y = -1
        self.width = 0
        self.height = 0
        self.alive = True
        self.awake = True
        self.mated = False
        self.mating = 0
        self.eaten = 0
        self.sleepTime = 0
        self.mate = None
        self.neighbors = {DIRECTION_NORTH:'?', DIRECTION_EAST:'?',
                          DIRECTION_SOUTH:'?', DIRECTION_WEST:'?'}
    
    # These methods are called by the simulater and not the critter
    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def is_alive(self):
        return self.alive

    def is_awake(self):
        if (self.awake == False):
            self.sleepTime += 1
            if self.sleepTime >= 10:
                self.sleepTime = 0
                self.awake = True
                self.wakeup()

        return self.awake

    def set_alive(self, alive):
        self.alive = alive

    def set_awake(self, awake):
        self.awake = awake

    def is_mating(self):
        if self.mated:
            if (self.mating >= 20):
                self.mate_end()
                return False
            else:
                self.mating += 1
                return True
        else:
            return False

    def get_mating(self):
        return self.mating > 0 and self.mating < 20

    def has_mated(self):
        return self.mated 

    def set_mated(self,boole):
        self.mated = boole

    def set_neighbor(self, direction, value):
        self.neighbors[direction] = value

    def get_neighbor(self, direction):
        # print(self.neighbors)
        return self.neighbors[direction]

    def increment_food(self):
        self.eaten += 1

    def get_food(self):
        return self.eaten

    def set_food(self):
        self.eaten = 0

    def win(self):
        return None

    def sleep(self):
        return None

    def mate(self):
        return None
    
    def reset(self):
        return None
    
    def lose(self):
        return None
    
    def wakeup(self):
        return None
    
    def mate_end(self):
        return None

    def set_mate(self,m):
        self.mate = m

    def get_mate(self):
        return self.mate
