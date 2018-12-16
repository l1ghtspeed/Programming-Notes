# Give the answers to the following runtimes:

def r1(n):
    l = []
    for i in range(n, 0, -1):
        l.append(lambda temp=i: temp)

    for f in l:
        for j in range(f()):
            print(j)

# Runtime of O(n^2)

def r2(n):
    l= []
    for i in range(n, 0, -1):
        l.append(lambda : i)

    for f in l:
        for j in range(f()):
            print(j)

# Runtime of O(n)