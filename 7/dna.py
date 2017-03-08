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
MASSES = [MASS_ADENINE, MASS_CYTOSINE, MASS_GUANINE, MASS_THYMINE]
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
        masses = percent_mass(counts, sequence)
        codons = find_codons(sequence)
        is_protein(codons, masses)
        print()


def read_data(data):
    file = open(data)
    lines = file.readlines()
    return lines


def count_nucleotides(sequence):
    counts = [0] * UNIQUE_NUCLEOTIDES
    for s in range(0, len(sequence)):
        c = sequence[s]
        if (c == "A"):
            counts[0] += 1
        elif (c == "C"):
            counts[1] += 1
        elif (c == "G"):
            counts[2] += 1
        elif (c == "T"):
            counts[3] += 1
    result = humanize_list(counts)
    print("Nuc. Counts: " + result)
    return counts


def percent_mass(counts, sequence):
    # Total up the mass of each nucleotide type
    mass = [0] * UNIQUE_NUCLEOTIDES
    total_mass = 0
    for m in range(0, len(mass)):
        mass[m] = counts[m] * MASSES[m]
        total_mass += mass[m]

    # Get the amount of junk
    junk = 0
    for j in range(0, len(sequence)):
        dash = sequence[j]
        if (dash == "-"):
            junk += 1
    junk_mass = junk * MASS_JUNK
    total_mass += junk_mass

    # Let's get the percents!
    percent_mass = [0] * UNIQUE_NUCLEOTIDES
    for p in range(0, len(percent_mass)):
        percent_mass[p] = round((mass[p] / total_mass) * 100, 1)
    result = humanize_list(percent_mass)
    print("Total Mass%: " + str(result) + " of " + str(round(total_mass, 1)))
    return percent_mass


def find_codons(sequence):
    c = []
    sequence = sequence.replace('-', '')
    for s in range(0, len(sequence), NUCLEOTIDES_PER_CODON):
        codon = sequence[s : s + NUCLEOTIDES_PER_CODON]
        c.append(codon)
    result = humanize_list(c)
    print("Codons List: " + result)
    return c


def is_protein(codons, masses):
    if ((codons[0].startswith("ATG")) and
        (codons[-1].startswith("TAA") or codons[-1].startswith("TAG") or codons[-1].startswith("TGA")) and
        (len(codons) >= MIN_CODONS) and
        (masses[1] + masses[2] >= PERCENTAGE_MASS_CG)):
        result = "YES"
    else:
        result = "NO"
    print("Is Protein?: " + result)


def humanize_list(inhuman_list):
    # loop through all peices of a list and output a nice, human-readable string!
    result = "["
    for i in range(0, len(inhuman_list)):
        if (i == len(inhuman_list) - 1):
            result += str(inhuman_list[i])
        else:
            result += str(inhuman_list[i]) + ", "
    result += "]"
    return result


def write_to_file(output, *args):
    out = open(output, "w")


main()
