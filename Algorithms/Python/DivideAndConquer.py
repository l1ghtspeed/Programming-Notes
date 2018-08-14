def mergeSort(a):
    newA = []
    if len(a) > 2:
        s1 = mergeSort(a[:int(len(a)/2)])
        s2 = mergeSort(a[int(len(a)/2):])
        n = len(s1) + len(s2)
        i = 0
        j = 0
        for k in range(n):
            if j >= len(s2):
                newA.append(s1[i])
                i += 1
            elif i >= len(s1):
                newA.append(s2[j])
                j += 1
            else:
                if s1[i] < s2[j]:
                    newA.append(s1[i])
                    i += 1
                else:
                    newA.append(s2[j])
                    j += 1
        return newA
    elif len(a) == 2:
        if a[0] < a[1]:
            return [a[0], a[1]]
        else:
            return [a[1], a[0]]
    else:
        return a[0]

print(mergeSort([3, 1, 2, 5, 2, 10, 2, 12]))


count = 0
def countInversions(a):
    global count
    newA = []
    if len(a) > 2:
        s1 = countInversions(a[:int(len(a)/2)])
        s2 = countInversions(a[int(len(a)/2):])
        n = len(s1) + len(s2)
        i = 0
        j = 0
        for k in range(n):
            if j >= len(s2):
                newA.append(s1[i])
                i += 1
            elif i >= len(s1):
                newA.append(s2[j])
                j += 1
            else:
                if s1[i] <= s2[j]:
                    newA.append(s1[i])
                    i += 1
                else:
                    newA.append(s2[j])
                    j += 1
                    count += len(s1) - i
        return newA
    elif len(a) == 2:
        if a[0] < a[1]:
            return [a[0], a[1]]
        else:
            return [a[1], a[0]]
    else:
        return a[0]

countInversions([1, 3, 5, 2, 4, 6])
print(count)