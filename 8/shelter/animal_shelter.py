# hours Spent: 2


def main():
    print("Welcome to animal shelter management software version 1.0!")
    done = False
    animals = []
    transfers = []
    adoptions = []
    files = ["pets.txt", "transferred.txt", "adopted.txt"]

    animals, transfers, adoptions = initiate(files)

    while (done == False):
        print("Type one of the following options:")
        print("adopt:    adopt a pet")
        print("intake:   add more animals to the shelter")
        print("list:     display all adoptable pets")
        print("quit:     exit the program")
        print("save:     save the current data")
        print("transfer: transfer pets to another shelter")
        
        option = input("option? ")

        if (option == "adopt"):
            animals, adoptions = adopt(animals, adoptions, files[0])
        elif (option == "intake"):
            intake_file = input("file? ")
            animals = intake(intake_file)
        elif (option == "list"):
            list_animals(animals)
        elif (option == "quit"):
            done = quit_asm(animals, transfers, adoptions)
        elif (option == "save"):
            save(animals, transfers, adoptions)
        elif (option == "transfer"):
            transfer_file = input("file name? ")
            animals, transfers = transfer(animals, transfers, transfer_file)

def initiate(files):
    # Read from all the files and return their contents
    for f in files:
        a = read_animals(f)
        if (f == 0):
            animals = a
        elif (f == 1):
            transfers = a
        elif (f == 2):
            adoptions = a
    return animals, transfers, adoptions

def adopt(animals, adoptions, filename):
    animal_type = input("animal type? ")
    name = input("name? ")
    # If type and name is in the list, remove it and add it to adopted

def intake(animals, filename):
    new = read_animals(filename)
    # TODO: Sort alphabetically on add
    for n in new:
        animals.append(n)
    return animals
    

def list_animals(animals):
    animal_type = input("cats, dogs or all? ")
    # List the selected option

def quit(animals, transfers, adoptions):
    # print shelter stats
    print(animals.count() + "pets currently in the shelter")
    print(adoptions.count() + "adopted")
    print(transfers.count() + "transferred")
    return True

def save(animals, transfers, adoptions, files):
    # write current shelter list, transferred list, and adopted list 
    # in original format, 
    for f in files:
        write_file = open(files[f])
        write_file.write()
        if (f == 0):
             = animals
        elif (f == 1):
             = transfers
        elif (f == 2):
             = adoptions

def transfer(animals, transfers, filename):
    trans = []
    f = open(filename)
    lines = f.readlines()
    for line in lines: 
        parts = line.lower().split()
        animal = (parts[0], parts[1], parts[2])
        trans.append(animal)
    # add to the transfer list, sorted alphabetically
    # remove from the animals list
    return animals, transfers

def read_animals(filename):
    f = open(filename)
    lines = f.readlines()
    for line in lines: 
        parts = line.lower().split()
        animal = (parts[0], parts[1], parts[2])
        animals.append(animal)
    return animals

main()