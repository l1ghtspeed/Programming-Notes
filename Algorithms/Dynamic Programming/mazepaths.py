# Problem: given a NxN grid, and certain obstacles, give the total number of possible paths to solve that maze.

# First implement naive recursive solution
sampleMaze = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]]

def solveMazeRecursion(s, t):
    if (s[0] >= len(sampleMaze)) or (s[1] >= len(sampleMaze[s[0]])) or (sampleMaze[s[0]][s[1]] == 1):
        return 0
    elif (s[0] == t[0]) and (s[1] == t[1]):
        return 1
    else:
        return solveMazeRecursion((s[0], s[1]+1), t) + solveMazeRecursion((s[0]+1, s[1]), t)


print(solveMazeRecursion((0, 0), (6, 5)))


# More efficient recursive solution
def solveMazeMemo(maze):
    totalPaths = 0
    return totalPaths

print(solveMazeMemo(sampleMaze))


# Most efficient solution, Dynamic Programming with bottom up approach
def solveMazeDP():
    newMaze = [[0]*len(sampleMaze[0])]*len(sampleMaze)
    newMaze[len(sampleMaze)-1][len(sampleMaze[0])-1] = 1
    for i in range(len(sampleMaze)-1, -1, -1):
        for j in range(len(sampleMaze[i])-1, -1, -1):
            print(i, j)
            print(newMaze[i][j])
            if (sampleMaze[i][j] != 1) and (newMaze[i][j] != 0):
                if (j != 0):
                    newMaze[i][j-1] += newMaze[i][j]
                if (i != 0):
                    newMaze[i-1][j] += newMaze[i][j]

    return newMaze[0][0]

print(solveMazeDP())

