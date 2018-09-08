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

def solve(n, edges, a, b):
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