# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: Animal Shelter
#
# A directory and management tool for animal shelters

# hours Spent: 5

ANIMALS = "pets.txt"
TRANSFERRED = "transferred.txt"
ADOPTED = "adopted.txt"


def main():
    print("Welcome to animal shelter management software version 1.0!")
    done = False
    animals = []
    transfers = []
    adoptions = []

    animals, transfers, adoptions = initiate()

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
            animals, adoptions = adopt(animals, adoptions)
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
            save(animals, transfers, adoptions)
            print()
        elif (option == "transfer"):
            transfer_file = input("file name? ")
            animals, transfers = transfer(animals,
                                          transfers,
                                          transfer_file)
            print()


# --------------------------------------------------------------------
# initiate() gets all the data previously saved by the program
#
# RETURNS:    the animals, transfers, and adoptions data
# --------------------------------------------------------------------
def initiate():
    # Read from all the files and return their contents
    animals = read_animals(ANIMALS)
    transfers = read_animals(TRANSFERRED)
    adoptions = read_animals(ADOPTED)
    return animals, transfers, adoptions


# --------------------------------------------------------------------
# adopt() adopts an animal from the shelter
#
# PARAMETERS: animals -- a list. animals in the shelter
#             adoptions -- a list. animals that have been adopted
# RETURNS:    updated lists of animals and adoptions
# --------------------------------------------------------------------
def adopt(animals, adoptions):
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


# --------------------------------------------------------------------
# intake() pulls in new animals into the shelter
#
# PARAMETERS: animals -- a list. animals in the shelter
#             filename -- a string. where the intake data exists
# RETURNS:    updated list of animals
# --------------------------------------------------------------------
def intake(animals, filename):
    new = read_animals(filename)
    for n in new:
        animals.append(n)
    animals.sort()
    return animals


# --------------------------------------------------------------------
# list_animals() lists animals currently in the shelter. It will list
#                all, only cats, or only dogs according to user input
#
# PARAMETERS: animals -- a list. animals in the shelter
# --------------------------------------------------------------------
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


# --------------------------------------------------------------------
# quit_asm() exits the program and displays statistics about animals
#            in, transferred, or adopted.
#
# PARAMETERS: animals -- a list. animals in the shelter
#             transfers -- a lits. animals that have been transferred
#             adoptions -- a list. animals that have been adopted
# RETURNS:    a boolean to initiate program exit
# --------------------------------------------------------------------
def quit_asm(animals, transfers, adoptions):
    # print shelter stats
    print(str(len(animals)) + " pets currently in the shelter")
    print(str(len(adoptions)) + " adopted")
    print(str(len(transfers)) + " transferred")
    return True


# --------------------------------------------------------------------
# save() saves the current data to files
#
# PARAMETERS: animals -- a list. animals in the shelter
#             transfers -- a lits. animals that have been transferred
#             adoptions -- a list. animals that have been adopted
# --------------------------------------------------------------------
def save(animals, transfers, adoptions):
    write_file(animals, ANIMALS)
    write_file(transfers, TRANSFERRED)
    write_file(adoptions, ADOPTED)


# --------------------------------------------------------------------
# transfer() transfers animals if the animals exist in the shelter
#
# PARAMETERS: animals -- a list. animals in the shelter
#             transfers -- a lits. animals that have been transferred
#             filename -- a string. file to get which animals will be
#                         transferred out of the shelter
# RETURNS: updated animal and transfers data
# --------------------------------------------------------------------
def transfer(animals, transfers, filename):
    trans = read_animals(filename)
    for t in trans:
        for a in animals:
            if a == t:
                animals.remove(a)
                transfers.append(t)
    animals.sort()
    transfers.sort()
    return animals, transfers


# --------------------------------------------------------------------
# read_animals() reads animal data from a specified file
#
# PARAMETERS: filename -- a string. file of animal data to read
#
# RETURNS: a list of animals retrieved from a file
# --------------------------------------------------------------------
def read_animals(filename):
    animals = []
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        if line != '':
            parts = line.lower().split()
            animal = (parts[0], parts[1], parts[2])
            animals.append(animal)
    animals.sort()
    return animals


# --------------------------------------------------------------------
# write_file() writes animal data to a specified file
#
# PARAMETERS: data -- a list. data to write to the file
#             filename -- a string. file of animal data to read
# --------------------------------------------------------------------
def write_file(data, filename):
    w = open(filename, 'w')
    for d in data:
        to_write = str(d[0] + " " + d[1] + " " + d[2])
        w.write(to_write + "\n")
    w.close()

main()
