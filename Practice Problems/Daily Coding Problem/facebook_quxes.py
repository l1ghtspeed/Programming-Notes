def num_remaining(quxes):
    if len(set(quxes)) == 1:
        return len(quxes)

    counts = {'R': 0, 'B': 0, 'G': 0}
    for qux in quxes:
        counts[quxes] += 1

    if counts['R'] % 2 == counts['B'] % 2 == counts['G'] % 2:
        return 2

    else:
        return 1
