from collections import deque
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        q = deque()
        solutions = []
        for i in range(n):
            s = set([_ for _ in range(n)])
            s.remove(i)
            q.append((s, set([(0, i)])))
        while q:
            cols, queens = q.popleft()
            row = len(queens)
            if row == n:
                solutions.append(self.generate_board(queens))
            for col in cols:
                attacked = False
                for queen in queens:
                    if abs(queen[0] - row) == abs(queen[1] - col):
                        attacked = True
                if not attacked:
                    new_cols = cols.copy()
                    new_cols.remove(col)
                    new_queens = queens.copy()
                    new_queens.add((row, col))
                    q.append((new_cols, new_queens))
        return solutions
    
    def generate_board(self, queens):
        solution = []
        for i in range(len(queens)):
            row = ""
            for j in range(len(queens)):
                if (i, j) not in queens:
                    row += "."
                else:
                    row += "Q"
            solution.append(row)
        return solution
