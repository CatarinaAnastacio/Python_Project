
def fastq_read(filename):
    """Reads a FastaQ file by given filename and returns a list with headers and a list with sequences
    Ignores the other non-necessary information"""
    headers = []
    sequences = []
    # Open the file
    infile = open(filename, 'r')
    for line in infile:
        if line.startswith('@'):
            headers.append(line.rstrip())
    infile.close()
    return headers, sequences


headers, sequences = fastq_read("Kleb-7-2-944_2_1_sequence.txt")

