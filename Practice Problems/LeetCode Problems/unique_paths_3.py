class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Set initial vars
        todo, self.ans, sy, sx, ey, ex = 0, 0, 0, 0, 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != -1: todo += 1
                if grid[i][j] == 1: sy, sx = i, j
                elif grid[i][j] == 2: ey, ex = i, j
        
        # brute dfs for paths
        def dfs(y, x, todo):
            todo -= 1
            if todo < 0: return
            if (y, x) == (ey, ex) and todo == 0: self.ans += 1
            grid[y][x] = -1
            for dy, dx in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                ny, nx = y+dy, x+dx
                if ny < len(grid) and ny >= 0 and nx < len(grid[ny]) and nx >= 0 and grid[ny][nx] != -1:
                    dfs(ny, nx, todo)
            grid[y][x] = 0
        
        dfs(sy, sx, todo)
        return self.ans
