
def countingValleys(n, s):
    altitude = 0
    count = 0
    for char in s:
        if char == 'U':
            altitude += 1
        elif char == 'D':
            altitude -= 1
            if altitude == -1:
                count += 1
    return count