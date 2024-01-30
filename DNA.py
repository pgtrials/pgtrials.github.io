# DNAseq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
def count_nucleotides(infile):
    """This function counts the number of all four nucleotides present in a sequence"""
    counts = {'A': 0, 'C': 0, 'T':0, 'G': 0}
    with open(infile, 'r') as file:
        seq = file.read()
        #sequence = seq.rstrip(seq[-1])
        nucleotides = [*seq]
        for nucleotide in nucleotides:
            if nucleotide in counts:
                counts[nucleotide] += 1

        counts_list = list(counts.values())
        print(*counts_list)
    pass


input_file = '/Users/pankti/Desktop/Bioinformatics/rosalind_solutions/input_data/rosalind_dna.txt'
'''#str = infile.readline()
print(count_nucleotides(input_file))
'''
with open(input_file, 'r') as f:
    f = f.read()
    num_A = f.count('A')
    num_T = f.count('T')
    num_C = f.count('C')
    num_G = f.count('G')
    print(num_A, num_C, num_G, num_T)

