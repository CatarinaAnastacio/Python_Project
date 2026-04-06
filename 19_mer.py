
def reading_dnaFasta (filename):
    Headers = []
    sequences = []

    infile = open(filename, 'r')
    seq = ''
    for line in infile:
        line = line.strip()
        if line and line[0] == '>':
            head = line[1:]
            Headers.append(head)
            if seq != '':
                sequences.append(seq)
                seq = ''
        else:
            seq += line 
    if seq != '':
            sequences.append(seq)

    infile.close()

    return Headers, sequences

Headers, sequences = reading_dnaFasta('resistance_genes.fsa.txt')

def reverse_com_strand(sequence):

    complementary_strand = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    
    reverse_com_strand = '' 

    for base in sequence[::-1]:
        if base in complementary_strand:
            reverse_com_strand += complementary_strand[base]
        else:
            reverse_com_strand += 'N'

    return reverse_com_strand

def nineteen(DNA):
    
    nineteen_mers = set()

    for i in range(len(DNA) - 18):
        fragment = DNA[i:i+19]
        nineteen_mers.add(fragment)
    return nineteen_mers

def k_mer_write(Headers, sequences, filename):
    outfile = open(filename, 'w')

    for i in range(len(sequences)):
        header = Headers[i]
        sequence = sequences[i]

        k_mer_foward = nineteen(sequence)

        rev_com = reverse_com_strand(sequence)
        rev_com_strand = nineteen(rev_com)

        outfile.write('>'+ header + '\n')
        outfile.write('Foward 19-mer:'+'\n')
        outfile.write(' '.join(k_mer_foward)+ '\n')
        outfile.write('Revere 19_mer:'+'\n')
        outfile.write(' '.join(rev_com_strand) + '\n\n')
    
    outfile.close

k_mer_output = k_mer_write(Headers, sequences, 'output_k_mer')
