# Complete the roverMove function below.
def roverMove(matrixSize, cmds):
    currSquare = [0, 0]
    for move in cmds:
        if move == 'RIGHT':
            if currSquare[1]+1 < matrixSize:
                currSquare[1] = currSquare[1]+1
        elif move == 'LEFT':
            if currSquare[1]-1 >= 0:
                currSquare[1] = currSquare[1]-1
        elif move == 'UP':
            if currSquare[0]-1 >= 0:
                currSquare[0] = currSquare[0]-1
        else:
            if currSquare[0]+1 < matrixSize:
                currSquare[0] = currSquare[0]+1
    return currSquare[0]*matrixSize + currSquare[1]