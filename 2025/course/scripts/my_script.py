# This script calculate the number of sequences in a fasta file
count = 0

with open('../data/input.fa', 'r') as fd:
    for line in fd:
        if line.startswith('>'):
            count += 1

print("The file contains", count, "sequences")
