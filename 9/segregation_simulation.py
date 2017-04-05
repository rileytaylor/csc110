# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: Segregation Simulation
#
# Simulates segregation by using Thomas Schelling's agent model

from drawingpanel import *
from random import *
from time import *


GRID_SIZE = 20
BOX_SIZE = 10
SQUARE_AXIS = BOX_SIZE * GRID_SIZE
PERCENTAGE_1 = 40
PERCENTAGE_2 = 35
COLOR_1 = "red"
COLOR_2 = "blue"
SPEED = 100
HAPPINESS_PERCENTAGE = 30

def main():
    panel = DrawingPanel(SQUARE_AXIS, SQUARE_AXIS, background="gray")

    agentsdb = create_agents()

    happy = False
    while (happy == False):
        panel.clear()
        draw_grid(panel, agentsdb)
        panel.sleep(100)
        happy = make_agents_happy(agentsdb)


def create_agents():
    db = []
    # Create Rows and Columns to match GRID_SIZE
    for i in range(0, GRID_SIZE):
        db.append([0] * GRID_SIZE)
    # Randomly place agents
    for row in db:
        for cell in range(0, len(row)):
            probability = randint(1, 100)
            if probability <= PERCENTAGE_1:
                row[cell] = 1
            elif (probability > PERCENTAGE_1 and
                 probability <= PERCENTAGE_2 + PERCENTAGE_1):
                row[cell] = 2
    return db


def make_agents_happy(db):
    to_move = []
    # For each cell, get the type of x, y and corners
    for row in range(0, len(db)):
        for cell in range(0, len(db[row])):
            agent = db[row][cell]
            # Find out how many of it's neighbors are the same, skip if empty
            if (agent != 0):
                neighbors = get_neighbors(db, row, cell)
                num_same = 0
                for n in neighbors:
                    if n == agent:
                        num_same += 1
                if not((num_same * 100 / 8) > HAPPINESS_PERCENTAGE):
                    to_move.append((row, cell))
    # if unhappy, move it
    if (len(to_move) == 0):
        return True
    else:
        for agent in to_move:
            move_agent(db, agent)
        return False


def get_neighbors(db, row, cell):
    ne = in_range(db, row - 1, cell - 1)
    n = in_range(db, row - 1, cell)
    nw = in_range(db, row - 1, cell + 1)
    w = in_range(db, row, cell + 1)
    sw = in_range(db, row + 1, cell + 1)
    s = in_range(db, row + 1, cell)
    se = in_range(db, row + 1, cell - 1)
    e = in_range(db, row, cell - 1)
    return ne, n, nw, w, sw, s, se, e


def in_range(db, row, cell):
    if not((row > GRID_SIZE - 1) or
           (cell > GRID_SIZE - 1) or
           (row < 0) or
           (cell < 0)):
        return db[row][cell]
    return 0


def move_agent(db, agent):
    # Get the value of the agent to move
    value = db[agent[0]][agent[1]]
    # Replace it's location with a 0 since it's leaving
    db[agent[0]][agent[1]] = 0
    #Traverse the grid for the first open spot after a random coordinate
    # starting_coord = (randint(0, 19), randint(0, 19))
    for row in db:
        for cell in range(0, len(row)):
            if row[cell] == 0:
                row[cell] = value
                return




# --------------------------------------------------------------------
# draw_cell() draws a square of a particular color.
#
# PARAMETERS: panel -- a variable. References the DrawingPanel
#             x -- an int. The starting x coordinate
#             y -- an int. The starting y coordinate
# --------------------------------------------------------------------
def draw_cell(panel, x, y, cell_data):
    if cell_data == 1:
        color = COLOR_1
    elif cell_data == 2:
        color = COLOR_2
    else:
        color = "white"
    panel.canvas.create_rectangle(x, y, x + BOX_SIZE, y + BOX_SIZE,
                                  fill=color, outline="black")


# --------------------------------------------------------------------
# draw_row() draws a row of a grid.
#
# PARAMETERS: panel -- a variable. References the DrawingPanel
#             y -- an int. The starting y coordinate
# --------------------------------------------------------------------
def draw_row(panel, y, row_data):
    x = 1
    for cell in row_data:
        draw_cell(panel, x, y, cell)
        x = x + BOX_SIZE


# --------------------------------------------------------------------
# draw_grid() draws a grid based on inputed data.
#
# PARAMETERS: panel -- a variable. References the DrawingPanel
# --------------------------------------------------------------------
def draw_grid(panel, grid_data):
    y = 1
    for row in grid_data:
        draw_row(panel, y, row)
        y = y + BOX_SIZE
    

main()
