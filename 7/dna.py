# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: DNA
#
# This program provides useful calculations on DNA input data

MIN_CODONS = 5
PERCENTAGE_MASS_CG = 30
UNIQUE_NUCLEOTIDES = 4
NUCLEOTIDES_PER_CODON = 3
MASS_ADENINE = 135.128
MASS_CYTOSINE = 111.103
MASS_GUANINE = 151.128
MASS_THYMINE = 125.107
MASS_JUNK = 100.000


def main():
    print("This program reports information about DNA\n",
          "nucleotide sequences that may encode protiens.")
    # data = input("Input file name? ")
    data = "dna.txt"
    # output = input("Output file name? ")
    sequences = read_data(data)
    for line in range(0, len(sequences), 2):
        name = sequences[line].strip()
        sequence = sequences[line + 1].strip().upper()
        print("Region Name: " + name)
        print("Nucleotides: " + sequence)
        counts = count_nucleotides(sequence)
        count_mass(counts)
        codons = find_codons(sequence)
        is_protein(codons)
        print()


def read_data(data):
    file = open(data)
    lines = file.readlines()
    return lines


def count_nucleotides(sequence):
    result = [0, 3, 50, 3]
    print("Nuc. Counts: " + "[",
          str(result[0]) + ",",
          str(result[1]) + ",",
          str(result[2]) + ",",
          str(result[3]) + "]")
    return result


def count_mass(nucelotide_count):
    result = [100.111, 100.111, 100.111, 100.111]
    print("Total Mass%: " + "[",
          str(result[0]) + ",",
          str(result[1]) + ",",
          str(result[2]) + ",",
          str(result[3]) + "]",
          " of " + str(result[0] + result[1] + result[2] + result[3]))


def find_codons(sequence):
    result = ['ATC', 'ATC', 'ATC', 'ATC', 'ATC']
    print("Codons List: " + "[",
          str(result[0]) + ",",
          str(result[1]) + ",",
          str(result[2]) + ",",
          str(result[3]) + ",",
          str(result[4]) + "]")
    return result


def is_protein(codons):
    result = "YES"
    print("Is Protein?: " + result)

# def humanize_lists(input):
#     loop through all peices of a list and output a nice HR string!

# def output_results(output, *args):
#     out = open(output, "w")


main()
