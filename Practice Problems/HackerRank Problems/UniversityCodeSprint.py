def speedLimites(s):
    n = int(s)
    if n <= 90:
        print('0 No punishment')
    elif n <= 110:
        print(str((n-90)*300)+ ' Warning')
    else:
        print(str((n-90)*500)+ ' License removed')

import itertools

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

from collections import deque

def abspecial(n, edges, a, b):
    d = {}
    q = deque()
    for i in range(1, n+1):
        d[i] = []
    
    for edge in edges:
        d[edge[0]].append(edge[1])
        d[edge[1]].append(edge[0])
    s = disjointset(n, d)
    for edge in edges:
        s.merge(edge[0], edge[1])
    s.findbounds()
    print(d)
    print(s.forest)
    count = 0
    for i in range(1, n+1):
        l = len(d[i])
        p = s.find(i)
        if l > a*s.minad[p] and l < b*s.maxad[p]:
            count += 1
    return count

        
          
            
class disjointset:
    def __init__(self, n, d):
        self.maxad = [0]*(n+1)
        self.minad = [1]*(n+1)
        self.forest = [0]*(n+1)
        self.rank = [0]*(n+1)
        for i in range(1, len(self.forest)):
            self.forest[i] = i
            self.maxad[i] = len(d[i])
            self.minad[i] = len(d[i])
            
    def merge(self, a, b):
        t1Parent = self.find(a)
        t2Parent = self.find(b)
        if (t1Parent != t2Parent):
            if (self.rank[t1Parent] > self.rank[t2Parent]):
                self.forest[t2Parent] = t1Parent
            else: 
                self.forest[t1Parent] = t2Parent
                if (self.rank[t1Parent] == self.rank[t2Parent]):
                    self.rank[t2Parent] += 1
    
    def findbounds(self):
        for i in range(1, len(self.forest)):
            p = self.find(i)
            if self.maxad[i] > self.maxad[p]:
                self.maxad[p] = self.maxad[i]
            else:
                self.maxad[i] = self.maxad[p]
                
            if self.minad[i] < self.minad[p]:
                self.minad[p] = self.minad[i]
            else:
                self.minad[i] = self.minad[p]
        
    def find(self, value):
        if (self.forest[value] != value):
            self.forest[value] = self.find(self.forest[value])
        return self.forest[value]

# Complete the solve function below.
def limitXOR(a, k):
    ans = temp = x = 0
    n = len(a)
    root = Node()
    insert(root, x, 30)
    for i in range(n):
        temp = a[i]
        x ^= temp
        ans += query(root, x, 30, k)
        insert(root, x, 30)    
    
    return ans
    
    


def insert(root, n, level):
    if level == -1:
        return root
    
    if n&(1<<level):
        root.rC += 1
        if not root.right:
            root.right = Node()
        root.right = insert(root.right, n, level-1)
    else:
        root.lC += 1
        if not root.left:
            root.left = Node()
        root.left = insert(root.left, n, level-1)

    return root

def query(root, n, level, k):
    if not root or level == -1:
        return 0
       
    p = bool(n&(1<<level))
    q = bool(k&(1<<level))
    
    if q:
        if not p:
            return root.lC+query(root.right, n, level-1, k)
        else:
            return root.rC+query(root.left, n, level-1, k)
    else:
        if not p:
            return query(root.left, n, level-1, k)
        else:
            return query(root.right, n, level-1, k)
        
    
class Node():
    def __init__(self):
        self.right = None
        self.left = None
        self.lC = 0
        self.rC = 0

# Complete the solve function below.
def cubelovingnumbers(n):
    primes = []
    count = 0
    for i in range(2, int(n**(1.0/3))+1):
        if isPrime(i):
            count += n//(i**3)
            for j in primes:
                l = lcm((j**3), (i**3))
                if l and l <= n:
                    count -= n//l
            primes.append(i)
    return count
        

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
    lcm = (x*y)//gcd(x,y)
    return lcm

import heapq
# Complete the solve function below.
def interestingTrip(n, roads, names, s, f):
    pq = []
    d = {}
    for i in range(n+1):
        d[i] = []
    for edge in roads:
        d[edge[0]].append(edge[1])
        
    # input for pq: (path weight, [node, pathstring])
    heapq.heappush(pq, (0, [s, '']))
    while pq:
        node = heapq.heappop(pq)
        if node[1][0] == f:
            return node[1][1]+names[node[1][0]-1]
        for neighbor in d[node[1][0]]:
            heapq.heappush(pq, ((ord(names[neighbor-1])-96)*(n-len(node[1][1]))*26, [neighbor, node[1][1]+names[node[1][0]-1]]))
    return 'No way'
