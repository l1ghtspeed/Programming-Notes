from collections import defaultdict

def create_map(pairs):
    words = set(sum(pairs, ()))
    n = len(words)

    synonyms = DisjointSet(words, n)

    for x, y in pairs:
        synonyms.union(x, y)

    return synonyms.sets

def compare(s1, s2, pairs):
    synonyms = create_map(pairs)

    w1 = s1.split(); w2 = s2.split()

    for x, y in zip(w1, w2):
        if x == y:
            continue
        elif x in synonyms and y in synonyms and synonyms[x] == synonyms[y]:
            continue
        else:
            return False
