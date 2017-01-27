# Author:  Riley Taylor
# Course:  CSC 110, Section 2J
# Program: ASCII Art
#
# This prints a lovely, perfect tree.

# tree_body() draws the upper cone of the tree.
def tree_body():
    for line in range(1, 10):
        repeat(" ", -1 * line + 10)
        repeat("A", 2 * line)
        repeat(" ", -1 * line + 10)
        print("")

# tree_trunk() just draws a tree trunk.abs
def tree_trunk():
    for line in range(1,3):
        print("      ", end='')
        print("[[]]")

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
    tree_body()
    tree_trunk()

main()
