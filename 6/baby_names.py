# Header

from drawingpanel import *

STARTING_YEAR = 1890
COLUMN_WIDTH = 60
LEGEND_HEIGHT = 30


def main():
    print("This program allows you to search through the\n"
          "data from the Social Security Administration\n"
          "to see how popular a particular name has been\n"
          "since 1890.\n")
    name = input("Name: ")
    gender = input("Gender: ")
    match = find_name("names.txt", name, gender)
    meaning = find_meaning("meanings.txt", name, gender)
    if (match == ""):
        match = '"' + name + '" not found.'
        print(match)
    else: 
        print(match + meaning)
        p = DrawingPanel(780, 560, "white")
        # draw_basics(p, meaning)
        # draw_histogram(p, match)


def find_name(fname, name, gender):
    f = open(fname)
    names = f.readlines()
    match = ""
    for n in names:
        if (n.lower().startswith(name.lower() + " " + gender[0].lower())):
            match = n
    return match

def find_meaning(fname, name, gender):
    m = open(fname)
    meanings = m.readlines()
    for m in meanings:
        if (m.startswith(name.upper() + " " + gender[0].lower())):
            return m
        elif (m.startswith(name.upper() + " mf")):
            return m


# def draw_basics(p, meaning_line):


# def draw_histogram(p, name_line):

main()
