def gc_content_batch(sequences):
    gc_contents = []
    for seq in sequences:
        seq = seq.upper()
        valid = [b for b in seq if b in "ATGC"]
        total = len(valid)
        if total == 0:
            gc_contents.append(0.0)
        else:
            gc = sum(1 for b in valid if b in "GC")
            gc_contents.append((gc/total)*100)
    return gc_contents

sequences = ["ATGCGC", "atttggc", "NNNNNN", "GATTACA", "CGCGCG"]
seq = ','.join(sequences)
results = gc_content_batch(sequences)
print(results)