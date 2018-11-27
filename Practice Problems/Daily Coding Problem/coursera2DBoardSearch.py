'''

This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.

'''

# This is kinda like a cheeky BFS algorithm question that's dressed up in a fun way
from collections import deque

def exists(board, word):
    queue = deque()
    seen = set()
    if not word or not board or not board[0]:
        return False
    for i in range(len(board)):
        for j in range(len(i)):
            if (word[currentLetter] == board[i][j]):
                currentLetter += 1
                queue.append(((i, j), 1))
    while queue:
        node = queue.popleft()
        x = node[0][0]
        y = node[0][1]
        if node[1] == len(word)
            return True
        else:
            if x+1 < len(board):
                if board[x+1][y] == word[node[1]] and (x+1, y) not in seen:
                    queue.append((x+1, y), node[1]+1)
                    seen.add((x+1, y))
            if x-1 >= 0:
                if board[x-1][y] == word[node[1]] and (x-1, y) not in seen: 
                    queue.append((x-1, y), node[1]+1)
                    seen.add((x-1, y))
            if y+1 < len(board[x]):
                if board[x][y+1] == word[node[1]] and (x, y+1) not in seen:
                    queue.append((x, y+1), node[1]+1)
                    seen.add((x, y+1))
            if y-1 >= 0:
                if board[x][y-1] == word[node[1]] and (x, y-1) not in seen: 
                    queue.append((x, y-1), node[1]+1)
                    seen.add((x, y-1))
    return False