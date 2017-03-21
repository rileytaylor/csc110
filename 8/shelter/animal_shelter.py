# hours Spent: 2


def main():
    print("Welcome to animal shelter management software version 1.0!")
    done = False
    animals = []
    transfers = []
    adoptions = []
    files = ("pets.txt", "transferred.txt", "adopted.txt")

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
            animals = intake(intake_file, filename)
        elif (option == "list"):
            list_animals(animals)
        elif (option == "quit"):
            done = quit_asm(animals, transfers, adoptions)
        elif (option == "save"):
            save(animals, transfers, adoptions, files)
        elif (option == "transfer"):
            transfer_file = input("file name? ")
            animals, transfers = transfer(animals, transfers, transfer_file)

def initiate(files):
    # Read from all the files and return their contents
    for f in range(0, len(files)):
        a = read_animals(files[f])
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


# DONE
def list_animals(animals):
    animal_type = input("cats, dogs or all? ")
    # List the selected option
    if (animal_type == "all"):
        for a in range(0, len(animals)):
            print(animals[a])
    elif (animal_type == "cats"):
        for a in range(0, len(animals)):
            animal = animals[a]
            if animal[0].lower() == 'cat':
                print(animals[a])
    elif (animal_type == "dogs"):
        for a in range(0, len(animals)):
            animal = animals[a]
            if animal[0].lower() == 'dog':
                print(animals[a])
    print()
                

# DONE
def quit_asm(animals, transfers, adoptions):
    # print shelter stats
    print(str(len(animals)) + " pets currently in the shelter")
    print(str(len(adoptions)) + " adopted")
    print(str(len(transfers)) + " transferred")
    return True

def save(animals, transfers, adoptions, files):
    # write current shelter list, transferred list, and adopted list 
    # in original format, 
    for f in range(0, len(files)):
        write_file = open(files[f], 'w')
        if (f == 0):
             write_file.write(animals)
        elif (f == 1):
             write_file.write(transfers)
        elif (f == 2):
             write_file.write(adoptions)

def transfer(animals, transfers, filename):
    trans = read_animals(filename)
    # add to the transfer list, sorted alphabetically
    # remove from the animals list
    return animals, transfers

def read_animals(filename):
    animals = []
    f = open(filename)
    lines = f.readlines()
    for line in lines: 
        parts = line.lower().split()
        animal = (parts[0], parts[1], parts[2])
        animals.append(animal)
    return animals

main()