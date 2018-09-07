def speedLimites(s):
    n = int(s)
    if n <= 90:
        print('0 No punishment')
    elif n <= 110:
        print(str((n-90)*300)+ ' Warning')
    else:
        print(str((n-90)*500)+ ' License removed')

def arrayTriplets(a):
    s = []
    length = len(a)
    for j in range(1, length-1):
        for k in range(j+1, length):
            if len(a[k:]) >= len(a[j:k]) and len(a[k:]) >= len(a[:j]) and len(a[j:k]) >= len(a[:j]):
                p = len(a[:j])
                q = len(a[j:k])
                r = len(a[k:])
                s.append([p, q, r])
    count = 0
    for triplet in s:
        temp = range(length)
        for p in itertools.combinations(temp, triplet[0]):
            temp1 = [x for x in temp if x not in p]
            for q in itertools.combinations(temp1, triplet[1]):
                temp2 = [x for x in temp1 if x not in q]
                for r in itertools.combinations(temp2, triplet[2]):
                    if (isValid(a, [p, q, r])):
                        count += 1
    return count
                

    
def isValid(a, l):
    return summ(a, l[0]) == summ(a, l[1]) == summ(a, l[2])
    
def summ(a, s):
    count = 0
    for i in s:
        count += a[i]
    return count