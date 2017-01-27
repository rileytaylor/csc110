SIZE = 4

def cone():
    for line in range(1, SIZE * 2 - 1)


def second_stage():
    

def first_stage():

def nozzle():

def connector():
    print("+", end='')
    repeat("=*", 2 * SIZE)
    print("+")

def top_diamond():
    for line in range(1, SIZE * 2)
        print("|", end='')
        repeat(".", -2 * line + 2 * SIZE + 1)
        repeat("//\\", )
        repeat(".", )
        repeat(".", )
        repeat("//\\", )
        repeat(".", )
        print("|", end='')

def bottom_diamond():


def repeat(string, count):
    for i in range(count):
        print(string, end='')

def main():
    cone()
    connector()
    second_stage()
    connector()
    first_stage()
    connector()
    nozzle()

main()