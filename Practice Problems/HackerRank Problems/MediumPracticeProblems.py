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

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    x = r_q
    y = c_q
    paths = [x-1, (x-1 if x < (n-y) else n-y-1), n-y, (n-x if x > y else n-y), n-x, (x-1 if x < y else y-1), y-1, (n-x if x > (n-y) else y)]
    
    for i in obstacles:
            #Check left path
        if((i[1] == y) and (i[0]-1 < paths[0])):
            paths[0] = x - i[0]
            #Check right path
        elif (i[1] == y) and (n-i[0] < paths[3]):
            paths[3] = i[0] - x
            #Check top path
        elif (i[0] == x) and (n-i[1] < paths[1]):
            print('lol')
        
    totaltiles = 0
    for i in paths:
        totaltiles += i
    return totaltiles


def appendAndDelete(s, t, k):
    if((k >= len(s)+len(t)) or (s == t and k == 0)):
        return 'Yes'
    
    tempS = s
    tempT = t
    
    num = len(t)
    
    if (len(s) < len(t)):
        num = len(s)

    for i in range(num):
        if(s[i] == t[i]):
            tempS = tempS[1:]
            tempT = tempT[1:]
        else:
            break
                
    leng = len(tempS)+len(tempT)
    if (leng == k):
        return 'Yes'
    elif ((leng < k) and ((k-leng)%2 == 0)):
        return 'Yes'
    else:
        return 'No'
