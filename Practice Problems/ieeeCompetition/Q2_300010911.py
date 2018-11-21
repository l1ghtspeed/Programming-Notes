# Rename file to Q2_<your student number>
# A is a list of integers
def songPairs(A):
    d = {}
    count = 0
    for duration in A:
        seconds = 60-(duration%60)
        if duration in d:
            count += d[duration]
        if seconds not in d:
            d[seconds] = 1
        else:
            d[seconds] += 1
        
    return count
