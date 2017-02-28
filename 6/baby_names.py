# Header


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
    find_name("names.txt", name, gender)


def find_name(fname, name, gender):
    f = open(fname)
    names = f.readlines()
    g = gender[0]
    match = ""
    for n in names:
        if (n.lower().startswith(name.lower() + " " + g.lower())):
            match = n
    return match
    



def draw_basics(p, meaning_line):


def draw_histogram(p, name_line):