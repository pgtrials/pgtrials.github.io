"""
Transcribing DNA to RNA
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t
."""
def DNAtoRNA(t):
    RNA = t.replace('T', 'U')
    return RNA

input_file = '/Users/pankti/Desktop/Bioinformatics/rosalind_solutions/input_data/rosalind_rna.txt'
with open(input_file, 'r') as file:
    t = file.read()
print(DNAtoRNA(t))
