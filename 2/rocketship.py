# Author:  Riley Taylor
# Course:  CSC 110, Section 2J
# Program: Rocket Ship
#
# This outputs an ascii rocket based on a size.

SIZE = 3

# cone() draws the cone shape used by the rocket's engine nozzle and
# the nose.
def cone():
    for line in range(1, SIZE * 2):
        repeat(" ", -1 * line + SIZE * 2 + 1)
        repeat("/", 1 * line + 1)
        print("**", end='')
        repeat("\\", 1 * line + 1)
        repeat(" ", -1 * line + SIZE * 2 + 1)
        print("")

# second_stage() draws the upper section of the rocket.
def second_stage():
    top_diamond()
    bottom_diamond()

# first_stage() draws the lower section of the rocket.
def first_stage():
    bottom_diamond()
    top_diamond()

# connector() draws the line between each section of the rocket.
def connector():
    print("+", end='')
    repeat("=*", 2 * SIZE + 1)
    print("+")

# top_diamond() This draws the top half of a diamond shape, which 
# is used as part of the pattern of the rocket stages.
def top_diamond():
    for line in range(1, SIZE + 1):
        print("|", end='')
        repeat(".", -1 * line + SIZE + 1)
        repeat("/\\", line + 1)
        repeat(".", -1 * line + SIZE + 1)
        repeat(".", -1 * line + SIZE + 1)
        repeat("/\\", line + 1)
        repeat(".", -1 * line + SIZE + 1)
        print("|")

# bottom_diamond() This draws the bottom half of a diamond shape, 
# which is used as part of the pattern of the rocket stages.
def bottom_diamond():
    for line in range(1, SIZE + 1):
        print("|", end='')
        repeat(".", 1 * line)
        repeat("\\/", -1 * line + SIZE + 2)
        repeat(".", 1 * line)
        repeat(".", 1 * line)
        repeat("\\/", -1 * line + SIZE + 2)
        repeat(".", 1 * line)
        print("|")

#---------------------------------------------------------------------
# repeat() repeats a string for a <count> number of times.
#
# PARAMETERS: string -- a string. The character(s) to be repeated.
#             count  -- an int. The number of times to repeat.
#---------------------------------------------------------------------
def repeat(string, count):
    for i in range(1, count):
        print(string, end='')

def main():
    cone()
    connector()
    second_stage()
    connector()
    first_stage()
    connector()
    cone()

main()
