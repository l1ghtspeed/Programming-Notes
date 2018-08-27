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
        # The main DFS algorithm
        while stack:
            vertice = stack.pop()
            for neighbor in d[vertice]:
                if seen[neighbor] == 0:
                    stack.append(neighbor)
                    connectedComponents[iterator].append(neighbor)
            seen[vertice] = 1
        iterator += 1
        connectedComponents.append([])

    return connectedComponents

print(dfs([(1, 7), (1, 3), (7, 9), (5, 9), (4, 5), (6, 8), (2, 6)], 9))

# Classic implementation of breadth first search
def bfs():
    return 1

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



