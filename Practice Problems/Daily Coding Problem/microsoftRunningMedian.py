# Brute Force Method
import math
def solve(a):
    for i in range(len(a)):
        temp = sorted(a[0:i+1])
        if len(temp)%2 == 0:
            print((temp[math.floor(i/2)]+temp[math.ceil(i/2)])/2)
        else:
            print(temp[int(i/2)])

#solve([2, 1, 5, 7, 2, 0, 5])

# Efficient Method
import heapq

def efficient(a):
    minheap = []
    maxheap = []
    
    if a:
        minheap.append(a[0])
        print(a[0])
    else:
        print('No valid array')

    for i in range(1, len(a)):
        if maxheap:
            left = -1*heapq.heappop(maxheap)
        else:
            left = None
        right = heapq.heappop(minheap)

        if a[i] >= right:
            heapq.heappush(minheap, a[i])
        else:
            heapq.heappush(maxheap, -1*a[i])
            
        
        heapq.heappush(minheap, right)
        if left:
                heapq.heappush(maxheap, -1*left)

        if len(minheap) - len(maxheap) > 1:
            temp = heapq.heappop(minheap)
            heapq.heappush(maxheap, temp*-1)
        elif len(maxheap) - len(minheap) > 1:
            temp = -1*heapq.heappop(maxheap)
            heapq.heappush(minheap, temp)
    
        if i%2 == 0:
            if len(minheap) < len(maxheap):
                temp = -1*heapq.heappop(maxheap)
                heapq.heappush(maxheap, -1*temp)
            else:
                temp = heapq.heappop(minheap)
                heapq.heappush(minheap, temp)
        else:
            l = -1*heapq.heappop(maxheap)
            r = heapq.heappop(minheap)
            temp = (l+r)/2
            heapq.heappush(minheap, r)
            heapq.heappush(maxheap, -1*l)
        
        print(temp)

efficient([2, 1, 5, 7, 2, 0, 5])