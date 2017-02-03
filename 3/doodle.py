# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: Doodle
#
# This draws a litle doodle using the DrawingPanel library

from drawingpanel import *

def main():
    panel = DrawingPanel(400, 400, background="black")

    # panel.canvas.create_line(200, 100, 200, 350, fill="white")

    # panel.canvas.create_line(200, 260, 270, 220, fill="white")
    # panel.canvas.create_line(270, 220, 270, 160, fill="white")

    # panel.canvas.create_line(200, 190, 100, 240, fill="white")
    # # panel.canvas.create_line(300, 240, 300, 300, fill="white")
    panel.canvas.create_line(130, 85, 300, 240, fill="white", width=4)
    panel.canvas.create_line(200, 150, 200, 280, fill="white", width=4)
    panel.canvas.create_oval(180, 130, 220, 170, fill="white", outline="white")
    panel.canvas.create_oval(280, 220, 320, 260, fill="white", outline="white")
    panel.canvas.create_oval(180, 260, 220, 300, fill="white", outline="white")

main()