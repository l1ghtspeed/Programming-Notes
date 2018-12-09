#Q807

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lrSkyline = []
        tbSkyline = []
        count = 0
        
        for row in grid:
            lrSkyline.append(max(row))
        
        for i in range(len(grid)):
            currentLargest = 0
            for j in range(len(grid)):
                if grid[j][i] > currentLargest:
                    currentLargest = grid[j][i]
            tbSkyline.append(currentLargest)
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] < min(tbSkyline[j], lrSkyline[i]):
                    count += min(tbSkyline[j], lrSkyline[i]) - grid[i][j]
        
        return count