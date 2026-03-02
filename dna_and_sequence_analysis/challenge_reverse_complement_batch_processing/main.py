def reverse_complement_batch(sequences):
    complement_table = str.maketrans("ATCGatcg", "TAGCtagc")
    results = []
    for seq in sequences:
        filtered = [ch.upper() for ch in seq if ch.upper() in "ATCG"]
        if not filtered:
            results.append("")       # keep empty if no valid bases
            continue

        # 3) translate and 4) reverse
        joined = "".join(filtered)
        comp = joined.translate(complement_table)
        rev = comp[::-1]

        results.append(rev)

    return results

# Sample calls
batch1 = ["ATCG", "ggta", "ACGTN", "xyz", "AAGCCTT"]
result1 = reverse_complement_batch(batch1)
print(result1)

batch2 = ["", "NNNN", "AGCTAGC"]
result2 = reverse_complement_batch(batch2)
print(result2)
