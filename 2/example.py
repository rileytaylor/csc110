# Allison Obourn and Janalee O'Bagy
# CSc 110, Spring 2017
# Lecture 5

# Outputs an ASCII art image of a mirror that can be
# scaled by altering the SIZE constant

SIZE = 3

def main():
    line()
    top_half()
    bottom_half()
    line()

# outputs the mirror frame top/bottom
def line():
    print("#", end='')
    for i in range(1, 4 * SIZE + 1):
        print("=", end='')
    print("#")

# outputs the top half of the mirror    
def top_half():
    for line in range(1, SIZE + 1):
        print("|", end='')
        for i in range(1, -2 * line + 2 * SIZE + 1):
            print(" ", end='')
        print("<>", end='')
        for i in range(1, 4 * line - 4 + 1):
            print(".", end='')
        print("<>", end='')
        for i in range(1, -2 * line + 2 * SIZE + 1):
            print(" ", end='')
        print("|", end='')
        print()

# outputs the bottom half of the mirror
def bottom_half():
    for line in range(SIZE, 0, -1):
        print("|", end='')
        for i in range(1, -2 * line + 2 * SIZE + 1):
            print(" ", end='')
        print("<>", end='')
        for i in range(1, 4 * line - 4 + 1):
            print(".", end='')
        print("<>", end='')
        for i in range(1, -2 * line + 2 * SIZE + 1):
            print(" ", end='')
        print("|", end='')
        print()

    
main()