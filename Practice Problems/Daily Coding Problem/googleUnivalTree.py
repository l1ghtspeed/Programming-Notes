from queue import *

def solution(T):  
    arr = [1]*len(T)
    q = Queue(maxsize=0)
    q.put(1)
    while q:
        node = q.get()
        nodeLeft = node*2
        nodeRight = node*2+1
        if nodeLeft < len(T):
            q.put(nodeLeft)
            if T[nodeLeft-1] != T[node-1]:
                arr
            if nodeRight < len(T):
                q.put(nodeRight)

    return 0

