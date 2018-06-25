# File containing all the 'medium' level problems solved on HackerRank
# Function name is name of problem

def matchingStrings(strings, queries):
    arr = []
    for i in queries:
        k = 0
        for j in strings:
            if i == j:
                k+=1
        arr.append(k)
    return arr

