def solve(s1, s2):
    i1 = 0
    i2 = 0
    count = 0
    while i2 < len(s2):
        if s1[i1] == s2[i2]:
            count += i2 - i1
            if i1 + 1 < len(s1):
                i1 += 1
            else:
                count += len(s2) - i1
        i2 += 1
    return count

print(solve('kitten', 'sitting'))