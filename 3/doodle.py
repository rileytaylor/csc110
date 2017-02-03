# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: Doodle
#
# This draws a git logo using the DrawingPanel library

from drawingpanel import *


def main():
    panel = DrawingPanel(400, 400, background="white")

    # draw the background for the logo
    panel.canvas.create_polygon(200, 15, 385, 200,
                                200, 385, 15, 200,
                                fill="orangered", outline="white")

    # Draw the lines and ovals for the git logo
    panel.canvas.create_line(130, 85, 260, 200,
                             fill="white", width=8)
    panel.canvas.create_line(200, 150, 200, 280,
                             fill="white", width=8)
    panel.canvas.create_oval(180, 130, 220, 170,
                             fill="white", outline="white", width=4)
    panel.canvas.create_oval(240, 180, 280, 220,
                             fill="white", outline="white", width=4)
    panel.canvas.create_oval(180, 260, 220, 300,
                             fill="white", outline="white", width=4)

main()
