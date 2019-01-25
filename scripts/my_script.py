input_data = '../data/input.fa'
ouput_data = '../data/input.dna'

with open(input_data, 'r') as fd:
    with open(ouput_data, 'w') as out: 

        for line in fd:
            if not line.startswith('>'):
                out.write(line)
