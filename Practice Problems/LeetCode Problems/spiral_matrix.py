class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n, x, y, state, solution, mz, nz = len(matrix), len(matrix[0]), 0, 0, 0, [], 0, 0
        s = m*n
        n = n-1
        m = m-1
        while len(solution) < s:
            if state == 0:
                while x <= n:
                    solution.append(matrix[y][x])
                    x += 1
                mz += 1
                y = mz
                x -= 1
            elif state == 1:
                while y <= m:
                    solution.append(matrix[y][x])
                    y += 1
                n -= 1
                x = n
                y -= 1
            elif state == 2:
                while x >= nz:
                    solution.append(matrix[y][x])
                    x -= 1
                m -= 1
                y = m
                x += 1
            else:
                while y >= mz:
                    solution.append(matrix[y][x])
                    y -= 1
                nz += 1
                x = nz
                y += 1
                state = -1
            state += 1
        return solution        
                
