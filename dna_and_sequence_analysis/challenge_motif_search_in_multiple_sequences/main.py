def find_motif_positions(sequences, motif):
    result = {}
    motif_length = len(motif)
    for seq in sequences:
        positions = []
        for i in range(len(seq) - motif_length + 1):
            if seq[i:i+motif_length] == motif:
                positions.append(i)
        result[seq] = positions
    return result

def find_motif2_positions(sequences2, motif2):
    result2 = {}
    motif2_length = len(motif2)
    for seq2 in sequences2:
        positions2 = []
        for i in range(len(seq2) - motif2_length + 1):
            if seq2[i:i+motif2_length] == motif2:
                positions2.append(i)
        result2[seq2] = positions2
    return result2

sequences = ["ATGCGATATCG", "GATATATGCATATACTT"]
motif = "ATAT"
motif_positions = find_motif_positions(sequences, motif)
positions_var = motif_positions
print(positions_var)

sequences2 = ["AAAAA", "TTTTT"]
motif2 = "AA"
motif_positions2 = find_motif_positions(sequences2, motif2)
positions_var2 = motif_positions2
print(positions_var2)
