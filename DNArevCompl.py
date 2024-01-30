def DNAtoRNA(infile):
    """ This function reads the DNA sequence from the file and gives the complementary RNA strand"""
    complRNAbasepairs = {'A':'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    with open(infile, 'r') as file:
        DNA = file.read()
        for nucleotide in complRNAbasepairs.keys():
            compl = DNA.replace('T', 'a').replace('A', 't').replace('C', 'g').replace('G', 'c')
            DNACompl = compl.upper()
            DNArevCompl = DNACompl[::-1]
    return DNArevCompl

input_file = '/Users/pankti/Desktop/Bioinformatics/rosalind_solutions/input_data/rosalind_revc.txt'
print(DNAtoRNA(input_file))
