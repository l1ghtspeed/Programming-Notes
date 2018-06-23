# A Collection of all the 'easy' problems on Hacker Rank
# Function Name is name of problem solved

def simpleArraySum(ar):
    count = 0
    for i in ar:
        count+=i 
    return count

def CompleteTheTriplets(a, b):
    ap = 0
    bp = 0
    for i in range(3):
        if (a[i] < b[i]):
            bp += 1
        elif (a[i] > b[i]):
            ap += 1
    return str(ap) + str(bp)


def pickingNumbers(a):
    count = 0
    
    for i in a:
        uppercount = 0
        lowercount = 0
        for j in a:
            if j == i:
                uppercount+=1
                lowercount+=1
            elif j == i+1:
                uppercount+=1
            elif j == i-1:
                lowercount+=1
        if uppercount >= count:
            count = uppercount
        if lowercount >= count:
            count = lowercount
    return count

def countApplesAndOranges(s, t, a, b, apples, oranges):
    numApples = 0
    numOranges = 0
    for i in apples:
        if (a + i >= s and a + i <= t):
            numApples+=1
    for i in oranges:
        if (b + i >= s and b + i <= t):
            numOranges+=1
    print(numApples)
    print(numOranges)

def diagonalDifference(arr):
    sumA = 0
    sumB = 0
    for i in range(len(arr)):
        sumA += arr[i][i]
        sumB += arr[len(arr)-i-1][i]
    return abs(sumA-sumB)

def staircase(n):
    for i in range(1,  n+1):
        print((n-i)*' ' + i*'#')