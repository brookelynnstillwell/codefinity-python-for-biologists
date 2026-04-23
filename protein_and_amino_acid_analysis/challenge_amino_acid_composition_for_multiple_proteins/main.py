def amino_acid_compositions(sequences):
    valid_aas = set("ACDEFGHIKLMNPQRSTVWY")
    results = []
    for seq in sequences:
        seq = seq.upper()
        aa_counts = {}
        total = 0
        for aa in seq:
            if aa in valid_aas:
                aa_counts[aa] = aa_counts.get(aa, 0) + 1
                total += 1
        if total == 0:
            results.append({})
        else:
            comp_dict = {}
            for aa, cnt in aa_counts.items():
                comp_dict[aa] = (cnt / total) * 100
            results.append(comp_dict)
    return results


# Sample calls
seqs = [
    "MKTIIALSYIFCLVFADYKDDDDA",
    "GAVLIPFYWSTCMNQDEKRH",
    "MXXKZZ",
    ""
]
result = amino_acid_compositions(seqs)
print(result)


# Sample calls
seqs = [
    "MKTIIALSYIFCLVFADYKDDDDA",
    "GAVLIPFYWSTCMNQDEKRH",
    "MXXKZZ",
    ""
]
result = amino_acid_compositions(seqs)
print(result)
