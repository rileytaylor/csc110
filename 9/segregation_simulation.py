# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: Segregation Simulation
#
# 

from drawingpanel import *
from random import *


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
    happy = False

    panel = DrawingPanel(SQUARE_AXIS, SQUARE_AXIS, background="gray")

    while (happy == False):
        agentsdb = create_agents()
        draw_grid(panel, agentsdb)
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
    number_unhappy = 0
    happy = False
    # For each cell, get the type of x, y and corners
    for row in grid:
        for cell in range(0, len(row)):
            agent = row[cell]
            neighbors = get_neighbors(db, row, cell)
            # calculate how many are of the same type
            num_same = 0
            for n in neighbors:
                if neighbors[n] == agent:
                    num_same + 1
            if not (num_same * 8 / 100) > HAPPINESS_PERCENTAGE:
                number_unhappy + 1
                move_agent(db, row, cell)

    # if less than HAPPINESS_PERCENTAGE, move it to a random spot.
    # calculate the random spot by randomly picking a cell on the Grid
    # and traversing until the next 0
    # then replace it with this guy and make the old spot a 0
    # If an agent is unhappy, bump up the counter
    if (number_unhappy == 0):
        happy = True
    return happy


# TODO: REFACTOR THE SHIT OUT OF THIS
def get_neighbors(db, row, cell):
    # agent = db[row][cell]
    ne = db[row - 1] [cell - 1]
    n = db [row - 1] [cell]
    nw = db[row - 1] [cell + 1]
    w = db [row]     [cell + 1]
    sw = db[row + 1] [cell + 1]
    s = db [row + 1] [cell]
    se = db[row + 1] [cell - 1]
    e = db [row]     [cell - 1]
    neighbors = ne, n, nw, w, sw, s, se, e
    return neighbors


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