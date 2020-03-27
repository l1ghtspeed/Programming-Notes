import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        paths, n, seen = [(grid[0][0], (0, 0))], len(grid), {}
        while paths:
            val, node = heapq.heappop(paths)
            if node == (n-1, n-1): return val
            for x, y in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
                nx, ny = node[0] + x, node[1] + y
                if nx >= 0 and ny >= 0 and nx < n and ny < n and max(val, grid[nx][ny]) < seen.get((nx, ny), float('inf')):
                    heapq.heappush(paths, (max(val, grid[nx][ny]), (nx, ny)))
                    seen[(nx, ny)] = max(val, grid[nx][ny])
