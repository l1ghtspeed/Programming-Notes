# File containing all the 'medium' level problems solved on HackerRank
# Function name is name of problem
from collections import deque


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
    y = r_q
    x = c_q
    paths = [x-1, (x-1 if x < (n-y) else n-y), n-y, (n-x if x > y else n-y), n-x, (x-1 if x < y else y-1), y-1, (n-x if x > (n-y) else y-1)]
    print(paths)
    
    for i in obstacles:
        #Check right path
        print(i)
        print(paths)
        if (i[0] == y) and (i[1] - x > 0) and (i[1] - x <= paths[4]):
            paths[4] = i[1] - x
        
        #Check left path
        elif (i[0] == y) and (x - i[1] > 0) and (x - i[1] <= paths[0]):
            paths[0] = x - i[1] - 1
        
        #Check top path
        elif (i[1] == x) and (i[0] - y > 0) and (i[0] - y <= paths[2]):
            paths[2] = i[0] - y - 1
        
        #Check bottom path
        elif (i[1] == x) and (y - i[0] > 0) and (y - i[0] <= paths[6]):
            paths[6] = y - i[0] - 1

        #Check topleft path
        elif ((i[0]-x) == (-1*i[1]-y)) and (i[1] - y > 0) and (i[1] - y <= paths[1]):
            paths[1] = i[1] - y - 1
        
        #Check bottomright path
        elif ((i[0]-x) == (-1*i[1]-y)) and (i[0] - x > 0) and (i[0] - x <= paths[5]):
            paths[5] = i[0] - x - 1
        
        #Check topright path
        elif ((i[0]-x) == (i[1]-y)) and (i[1] - y > 0) and (i[1] - y <= paths[3]):
            paths[3] = i[1] - y - 1

        #Check bottomleft path
        elif ((i[0]-x) == (i[1]-y)) and (i[1] - y < 0) and (-1*(i[1] - y) <= paths[7]):
            paths[7] = -1*(i[1] - y) - 1

    totaltiles = 0
    for i in paths:
        totaltiles += i
    return totaltiles

    '''

    if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

    '''


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



def knightlOnAChessboard(n):
    sol = []
    for i in range(1, n):
        for j in range(1, n):
            sol.append(breadthFirstSearch((i,j), n))
            
    return sol

def breadthFirstSearch(moves, n):
    nodesQueue = deque()
    nodesQueue.appendleft([(0,0), 0])
    
    seen = []
    seen.append((0,0))
    
    while nodesQueue:
        currNode = nodesQueue.pop()
        move = currNode[1]
        
        if currNode[0] == (n-1, n-1):
            return move
        
        if appendable(n, currNode[0][0]+moves[0], currNode[0][1]+moves[1], seen):
            nodesQueue.appendleft([(currNode[0][0]+moves[0], currNode[0][1]+moves[1]), move+1])
            
        if appendable(n, currNode[0][0]+moves[0], currNode[0][1]-moves[1], seen):
            nodesQueue.appendleft([(currNode[0][0]+moves[0], currNode[0][1]-moves[1]), move+1])
            
        if appendable(n, currNode[0][0]-moves[0], currNode[0][1]-moves[1], seen):
            nodesQueue.appendleft([(currNode[0][0]-moves[0], currNode[0][1]-moves[1]), move+1])
            
        if appendable(n, currNode[0][0]-moves[0], currNode[0][1]+moves[1], seen):
            nodesQueue.appendleft([(currNode[0][0]-moves[0], currNode[0][1]+moves[1]), move+1])
            
        if appendable(n, currNode[0][0]+moves[1], currNode[0][1]+moves[0], seen):
            nodesQueue.appendleft([(currNode[0][0]+moves[1], currNode[0][1]+moves[0]), move+1])
            
        if appendable(n, currNode[0][0]+moves[1], currNode[0][1]-moves[0], seen):
            nodesQueue.appendleft([(currNode[0][0]+moves[1], currNode[0][1]-moves[0]), move+1])
            
        if appendable(n, currNode[0][0]-moves[1], currNode[0][1]-moves[0], seen):
            nodesQueue.appendleft([(currNode[0][0]-moves[1], currNode[0][1]-moves[0]), move+1])
            
        if appendable(n, currNode[0][0]-moves[1], currNode[0][1]+moves[0], seen):
            nodesQueue.appendleft([(currNode[0][0]-moves[1], currNode[0][1]+moves[0]), move+1])
    
    return -1
        

def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    nodesQueue = deque()
    nodesQueue.appendleft([(j_start, i_start), []])
    seen = []
    seen.append((i_start, j_start))
    while nodesQueue:
        currNode = nodesQueue.pop()
        if (currNode[0][0] == j_end) and (currNode[0][1] == i_end):
            temp = ''
            path = currNode[1]
            temp += str(len(path)) + '\n'
            for i in path:
                temp += i + ' '
            return temp
        else:
            if appendable(n, currNode[0][0]-1, currNode[0][1]-2, seen):
                path = list(currNode[1])
                path.append('UL')
                nodesQueue.appendleft([(currNode[0][0]-1, currNode[0][1]-2), path])
            
            if appendable(n, currNode[0][0]+1, currNode[0][1]-2, seen):
                path = list(currNode[1])
                path.append('UR')
                nodesQueue.appendleft([(currNode[0][0]+1, currNode[0][1]-2), path])
            
            if appendable(n, currNode[0][0]+2, currNode[0][1], seen):
                path = list(currNode[1])
                path.append('R')
                nodesQueue.appendleft([(currNode[0][0]+2, currNode[0][1]), path])
            
            if appendable(n, currNode[0][0]+1, currNode[0][1]+2, seen):
                path = list(currNode[1])
                path.append('LR')
                nodesQueue.appendleft([(currNode[0][0]+1, currNode[0][1]+2), path])
            
            if appendable(n, currNode[0][0]-1, currNode[0][1]+2, seen):
                path = list(currNode[1])
                path.append('LL')
                nodesQueue.appendleft([(currNode[0][0]-1, currNode[0][1]+2), path])
            
            if appendable(n, currNode[0][0]-2, currNode[0][1], seen):
                path = list(currNode[1])
                path.append('L')
                nodesQueue.appendleft([(currNode[0][0]-2, currNode[0][1]), path])
    
    return 'Impossible'
            

def appendable(n, a, b, seen):
    if (a < n) and (a >= 0) and (b < n) and (b >= 0) and ((a, b) not in seen):
        seen.append((a,b))
        return True
    return False
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)
    output = ''
    for i in range(len(result)):
        if ((i+1)%(n-1) == 0):
            output += str(result[i]) + '\n'
        else:
            output += str(result[i]) + ' '
    
    fptr.write(output)
        
    fptr.write('\n')

    fptr.close()


sum = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] >= 1:
                sum+=2
                #Left Neighbor
                if ((A[i-1][j] < A[i][j]) and (i-1 >= 0)):
                    sum += A[i][j]-A[i-1][j]
                elif i-1 < 0:
                    sum += A[i][j]
                #Right Neighbor
                if((i+1 < len(A)) and (A[i+1][j] < A[i][j])):
                    sum += A[i][j]-A[i+1][j]
                elif i+1 >= len(A):
                    sum += A[i][j]
                #Up Neighbor
                if((A[i][j-1] < A[i][j]) and (j-1 >= 0)):
                    sum += A[i][j] - A[i][j-1]
                elif j-1 < 0:
                    sum += A[i][j]
                #Down Neighbor
                if((j+1 < len(A[i])) and (A[i][j+1] < A[i][j])):
                    sum += A[i][j] - A[i][j+1]
                elif j+1 >= len(A[i]):
                    sum += A[i][j]
    return sum