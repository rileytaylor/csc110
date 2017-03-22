# hours Spent: 5

FILES = ("pets.txt", "transferred.txt", "adopted.txt")

def main():
    print("Welcome to animal shelter management software version 1.0!")
    done = False
    animals = []
    transfers = []
    adoptions = []

    animals, transfers, adoptions = initiate(FILES)

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
            animals, adoptions = adopt(animals, adoptions, FILES[0])
            print()
        elif (option == "intake"):
            intake_file = input("file? ")
            animals = intake(animals, intake_file)
            print()
        elif (option == "list"):
            list_animals(animals)
            print()
        elif (option == "quit"):
            done = quit_asm(animals, transfers, adoptions)
        elif (option == "save"):
            save(animals, transfers, adoptions, FILES)
            print()
        elif (option == "transfer"):
            transfer_file = input("file name? ")
            animals, transfers = transfer(animals,
                                          transfers,
                                          transfer_file)
            print()

# DONE
def initiate():
    # Read from all the FILES and return their contents
    for f in range(0, len(FILES)):
        a = read_animals(FILES[f])
        if (f == 0):
            animals = a
        elif (f == 1):
            transfers = a
        elif (f == 2):
            adoptions = a
    return animals, transfers, adoptions


# DONE
def adopt(animals, adoptions, filename):
    animal_type = input("animal type? ").lower()
    adoptee = input("name? ").lower()
    # If type and name is in the list, remove it and add it to adopted
    for a in animals:
        if (a[0].lower() == animal_type) and (a[1].lower() == adoptee):
            adoptee = a
            animals.remove(a)
            adoptions.append(adoptee)
    animals.sort()
    adoptions.sort()
    return animals, adoptions


# DONE
def intake(animals, filename):
    new = read_animals(filename)
    for n in new:
        animals.append(n)
    animals.sort()
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
                

# DONE
def quit_asm(animals, transfers, adoptions):
    # print shelter stats
    print(str(len(animals)) + " pets currently in the shelter")
    print(str(len(adoptions)) + " adopted")
    print(str(len(transfers)) + " transferred")
    return True


# DONE
def save(animals, transfers, adoptions):
    # write current shelter list, transferred list, and adopted list 
    # in original format, 
    write_file(animals, FILES[0])
    write_file(transfers, FILES[1])
    write_file(adoptions, FILES[2])


# DONE
def transfer(animals, transfers, filename):
    trans = read_animals(filename)
    # add to the transfer list, sorted alphabetically
    # remove from the animals list
    for t in trans:
        for a in animals:
            if a == t:
                animals.remove(a)
                transfers.append(t)
    animals.sort()
    transfers.sort()
    return animals, transfers


# DONE
def read_animals(filename):
    animals = []
    f = open(filename)
    lines = f.readlines()
    for line in lines: 
        parts = line.lower().split()
        animal = (parts[0], parts[1], parts[2])
        animals.append(animal)
    animals.sort()
    return animals

# DONE
def write_file(data, filename):
    w = open(filename, 'w')
    for d in data:
        w.write(str(d) + "\n")
    w.close()

main()