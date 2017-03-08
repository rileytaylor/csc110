# Author: Riley Taylor
# Course: CSC 110, Section 2J, Spring 2017
# Program: DNA
#
# This program provides useful statistics on DNA data

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
    data = input("Input file name? ")
    output = input("Output file name? ")
    sequences = read_data(data)
    for line in range(0, len(sequences), 2):
        name = get_name(sequences[line], output)
        sequence = get_sequence(sequences[line + 1], output)
        counts = count_nucleotides(sequence, output)
        masses = percent_mass(counts, sequence, output)
        codons = find_codons(sequence, output)
        is_protein(codons, masses, output)
        write_to_file(output, "")


# --------------------------------------------------------------------
# read_data() retrieves the dna data from it's file
#
# PARAMETERS: data -- a string. the file
# --------------------------------------------------------------------
def read_data(data):
    file = open(data)
    lines = file.readlines()
    return lines


# --------------------------------------------------------------------
# get_name() retrieves the name and prints it to the output file
#
# PARAMETERS: line -- a string. the name line
#             output -- a string. The output file
# RETURNS:    the name as a string
# --------------------------------------------------------------------
def get_name(line, output):
    name = line.strip()
    write_to_file(output, "Region Name: " + name)
    return name


# --------------------------------------------------------------------
# get_sequence() retrieves the sequence and prints it to the output
#                file
#
# PARAMETERS: line -- a string. the sequence line
#             output -- a string. The output file
# RETURNS:    the sequence as a string
# --------------------------------------------------------------------
def get_sequence(line, output):
    sequence = line.strip().upper()
    write_to_file(output, "Nucleotides: " + sequence)
    return sequence


# --------------------------------------------------------------------
# count_nucleotides() counts the amount of each nucleotide in a
#                     dna sequence
#
# PARAMETERS: sequence -- a string. the sequence
#             output -- a string. The output file
# RETURNS:    a list of codon counts
# --------------------------------------------------------------------
def count_nucleotides(sequence, output):
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
    write_to_file(output, "Nuc. Counts: " + result)
    return counts


# --------------------------------------------------------------------
# percent_mass() calculates the mass percentageof each nucleotide in a
#                dna sequence, including the junk.
#
# PARAMETERS: counts -- a list. the nucleotide counts
#             sequence -- a string. the sequence
#             output -- a string. The output file
# RETURNS:    a list of codon masses as a percentage of the total
# --------------------------------------------------------------------
def percent_mass(counts, sequence, output):
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
    write_to_file(output, "Total Mass%: " +
                  str(result) + " of " +
                  str(round(total_mass, 1)))
    return percent_mass


# --------------------------------------------------------------------
# find_codons() finds the codons and outputs a list of them
#
# PARAMETERS: sequence -- a string. the sequence
#             output -- a string. The output file
# RETURNS:    a list of codons
# --------------------------------------------------------------------
def find_codons(sequence, output):
    c = []
    sequence = sequence.replace('-', '')
    for s in range(0, len(sequence), NUCLEOTIDES_PER_CODON):
        codon = sequence[s: s + NUCLEOTIDES_PER_CODON]
        c.append(codon)
    result = humanize_list(c)
    write_to_file(output, "Codons List: " + result)
    return c


# --------------------------------------------------------------------
# is protein() evaluates whether a sequence is a protein
#
# PARAMETERS: codons -- a list. a list of codons present in a sequence
#             masses -- a list. a list of masses by percentage
#             output -- a string. The output file
# --------------------------------------------------------------------
def is_protein(codons, masses, output):
    if ((codons[0].startswith("ATG")) and
        (codons[-1].startswith("TAA") or
         codons[-1].startswith("TAG") or
         codons[-1].startswith("TGA")) and
        (len(codons) >= MIN_CODONS) and
        (masses[1] + masses[2] >= PERCENTAGE_MASS_CG)):
        result = "YES"
    else:
        result = "NO"
    write_to_file(output, "Is Protein?: " + result)


# --------------------------------------------------------------------
# humanize_list() makes a human readable string from a list
#
# PARAMETERS: inhuman_list -- a list. the list to be humanized
# RETURNS:    a string
# --------------------------------------------------------------------
def humanize_list(inhuman_list):
    result = "["
    for i in range(0, len(inhuman_list)):
        if (i == len(inhuman_list) - 1):
            result += str(inhuman_list[i])
        else:
            result += str(inhuman_list[i]) + ", "
    result += "]"
    return result


# --------------------------------------------------------------------
# write_to_file() writes a string to the specified output file
#
# PARAMETERS: file -- a string. the file to open
#             text -- a string. The string to write to the output file
# --------------------------------------------------------------------
def write_to_file(file, text):
    outFile = open(file, "a")
    outFile.write(text + "\n")
    outFile.close()


main()
