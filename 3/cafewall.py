# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: Cafe Wall
#
# This draws several rows of black and white boxes, as well as several examples
# of the Cafe Wall illusion.

from drawingpanel import *

MARGIN = 2
# TODO: Need to incorporate the Margin somewhere!

def main():
    panel = DrawingPanel(650, 400, background="gray")

    draw_grid(panel, 1, 0, 0, 4, 20, 0)

#---------------------------------------------------------------------
# box() draws a box of a particular color. If it is a black box it will also add
# a blue 'X'
#
# PARAMETERS: panel -- a variable. References the DrawingPanel
#             x -- an int. The starting x coordinate
#             y -- an int. The starting y coordinate
#             size  -- an int. The size of the box
#             color -- a string. The color of the box
#---------------------------------------------------------------------
def box(panel, x, y, size, color):
    panel.canvas.create_rectangle(x, y, x + size, y + size, background=color)
    if (color == "black"):
        panel.canvas.draw_line()
        panel.canvas.draw_line()

# Draw's a row of a specified length. The count represents a pair.
def draw_row(panel, count, x, y, size, offset):
    # TODO: Need to actually add an offset, probs with an if statement
    # that gives it a bit of a margin before drawing the boxes
    for pair in range(0, count):
        box(panel, x, y, size, "black")
        # Add the size to make up for the black box, might need to add 1?
        box(panel, x + size, y + size, size, "white")

def draw_grid(panel, rows, row_length, x_start, y_start, box_size, offset):
    for row in range(0, rows):
        draw_row(panel, row_length, x_start, y_start, box_size, offset)

main()
