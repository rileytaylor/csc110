SIZE = 3

def cone():
    for line in range(1, SIZE * 2 - 1)


def second_stage():
    for line in range(1, SIZE * 2)
        print("|", end='')
        for i in range(2)
            repeat(".", )
            repeat("//\\", )
            repeat(".", )
        print("|", end='')

def first_stage():

def nozzle():

def connector():
    print("+", end='')
    repeat("=*", 2 * SIZE)
    print("+")

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