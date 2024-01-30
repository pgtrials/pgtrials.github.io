"""In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx",
where "xxxx" denotes a four-digit code between 0000 and 9999.
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers"""
infile = '/Users/pankti/Desktop/Bioinformatics/rosalind_solutions/input_data/rosalind_gc.txt'
with open(infile, 'r') as file:
        fasta_data = file.read()
def calculate_gc_content(dna):
    gc_count = sum(nucleotide in ('G', 'C') for nucleotide in dna)
    return (gc_count / len(dna)) * 100

def find_highest_gc_content(fasta_data):
    sequences = {}
    current_id = ""
    current_sequence = ""

    # Parse the FASTA data and store sequences in a dictionary
    for line in fasta_data.splitlines():
        if line.startswith(">"):
            if current_id and current_sequence:
                sequences[current_id] = current_sequence
            current_id = line[1:]
            current_sequence = ""
        else:
            current_sequence += line.strip()

    # Add the last sequence in the loop
    if current_id and current_sequence:
        sequences[current_id] = current_sequence

    # Calculate GC-content for each sequence
    highest_gc_id = ""
    highest_gc_content = 0

    for seq_id, dna_string in sequences.items():
        gc_content = calculate_gc_content(dna_string)
        if gc_content > highest_gc_content:
            highest_gc_id = seq_id
            highest_gc_content = gc_content

    return highest_gc_id, highest_gc_content

# Example usage:
result_id, result_gc_content = find_highest_gc_content(fasta_data)
print(result_id)
print(result_gc_content)
