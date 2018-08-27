# Graph type Greedy Algs

# Classic implementation of depth first search
def dfs(edges, n):
    '''
    Create a depth first search algorithm that creates an array of connected components
    Inputs:
        edges: list of tuples representing non-directed edges from vertices (vertices will be presented in order)
        n: number of vertices
    Output:
        List of lists representing all connected vertices
    '''

    # Initialize required elements
    stack = []
    seen = [0]*(n+1)
    d = {}
    connectedComponents = [[]]

    # Set up dictionary by preprocessing edges:
    for i in edges:
        if i[0] not in d:
            d[i[0]] = [i[1]]
        else:
            d[i[0]].append(i[1])
        if i[1] not in d:
            d[i[1]] = [i[0]]
        else:
            d[i[1]].append(i[0])


    # Loop through keys that are not yet seen:
    iterator = 0
    for key in d:
        if seen[key] == 0:
            connectedComponents[iterator].append(key)
            stack.append(key)
            seen[key] = 1
        # The main DFS algorithm
        while stack:
            vertice = stack.pop()
           
            for neighbor in d[vertice]:
                if seen[neighbor] == 0:
                    stack.append(neighbor)
                    seen[neighbor] = 1
                    connectedComponents[iterator].append(neighbor)
        iterator += 1
        connectedComponents.append([])

    return connectedComponents

print(dfs([(1, 7), (1, 3), (7, 9), (5, 9), (4, 5), (6, 8), (2, 6)], 9))

# Classic implementation of breadth first search
from collections import deque
def bfs(edges, n, a, b):
    '''
    Uses BFS to find shortest unweighted path in graph
    Inputs:
        edges: list of tuples representing non-directed edges from vertices (vertices will be presented in order)
        n: integer number of vertices
        a: integer starting location
        b: integer end location
    Output:
        Integer denoting the minimum number of steps taken, returns -1 if cannot be reached
    '''
    # Initialize required elements
    queue = deque()
    seen = [0]*(n+1)
    d = {}

    # Set up dictionary by preprocessing edges:
    for i in edges:
        if i[0] not in d:
            d[i[0]] = [i[1]]
        else:
            d[i[0]].append(i[1])
        if i[1] not in d:
            d[i[1]] = [i[0]]
        else:
            d[i[1]].append(i[0])
    
    # Add starting position to queue, track number of steps
    queue.append((a, 0))
    
    # Main bfs function
    while queue:
        key = queue.popleft()
        seen[key[0]] = 1
        for neighbor in d[key[0]]:
            if neighbor == b:
                return key[1] + 1
            if seen[neighbor] == 0:
                queue.append((neighbor, key[1]+1))
                seen[neighbor] = 1
    return -1

print(bfs([(1, 7), (1, 3), (7, 9), (5, 9), (4, 5), (6, 8), (2, 6), (1, 10), (11, 10), (4, 11)], 11, 6, 4))

# Classic implementation of Dijkstras
def dijkstras():
    return 0

# Finding strongly connected components in a directed graph (cycles graph)
def scc():
    return 1

# Find whether it is possible to get from A to B using Union Find (Disjoint Set)
def mazeSolve():
    return 0

# Classic implementation of Prim's MST
def prims():
    return 1

# Classic implementation of Floyd Warshall Alg for finding All Pairs shortest path
def fw():
    return 0

# Find "bridges" in graph - nodes that are connect to a graph by only one edge
def bridge():
    return 1



