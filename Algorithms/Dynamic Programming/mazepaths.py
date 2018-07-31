# Problem: given a NxN grid, and certain obstacles, give the total number of possible paths to solve that maze.

# First implement naive recursive solution
sampleMaze = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0]]

def solveMazeRecursion(maze):
    totalPaths = 0
    return totalPaths

print(solveMazeRecursion(sampleMaze))


# More efficient recursive solution
def solveMazeMemo(maze):
    totalPaths = 0
    return totalPaths

print(solveMazeMemo(sampleMaze))


# Most efficient solution
def solveMazeDP(maze):
    totalPaths = 0
    return totalPaths

print(solveMazeDP(sampleMaze))

