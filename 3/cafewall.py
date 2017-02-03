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

    draw_grid(panel, 1, 4, 0, 0, 20, 0)
    draw_grid(panel, 1, 5, 50, 70, 30, 0)
    draw_grid(panel, 8, 4, 10, 150, 25, 0)
    draw_grid(panel, 6, 3, 250, 200, 25, 10)
    draw_grid()

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
    panel.canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline=color)
    # if (color == "black"):
    #     panel.canvas.draw_line()
    #     panel.canvas.draw_line()

# Draw's a row of a specified length. The count represents a pair.
def draw_row(panel, count, x, y, size, offset):
    for pair in range(1, count):
        box(panel, x, y, size, "black")
        box(panel, x + size + 1, y, size, "white")
        x = x + size * 2

def draw_grid(panel, rows, row_length, x_start, y_start, box_size, offset):
    for row in range(1, rows + 1):
        # TODO: Add offset
        if ((row % 2 == 0) and offset > 0):
            x_start = x_start + offset
        draw_row(panel, row_length, x_start, y_start, box_size, offset)
        y_start = y_start + box_size + MARGIN

main()
