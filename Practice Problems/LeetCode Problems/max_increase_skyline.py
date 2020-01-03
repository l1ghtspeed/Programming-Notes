#Q807
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        x, y, count = len(grid), len(grid[0]), 0
        rows, cols = [0 for _ in range(x)], [0 for _ in range(y)]
        for i in range(x):
            for j in range(y):
                rows[i] = max(rows[i], grid[i][j])
                cols[j] = max(cols[j], grid[i][j])
        
        for i in range(x):
            for j in range(y):
                count += min(cols[j], rows[i]) - grid[i][j]
        
        return count
