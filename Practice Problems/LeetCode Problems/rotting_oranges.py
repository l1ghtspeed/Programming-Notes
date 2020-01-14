from copy import deepcopy
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count, changed, new_grid = 0, True, deepcopy(grid)
        if not grid or not grid[0]:
            return -1
        while changed:
            changed = False
            count += 1
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        for x, y in zip([0, 0, -1, 1], [1, -1, 0, 0]):
                            new_x, new_y = x + i, y + j
                            if new_x < len(grid) and new_x >= 0 and new_y < len(grid[0]) and new_y >= 0 and grid[new_x][new_y] == 1:
                                new_grid[new_x][new_y] = 2
                                changed = True
            grid = deepcopy(new_grid)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
    
        return count - 1
                            
