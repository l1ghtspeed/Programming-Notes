class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans, min_r, max_c, x, y = [], [], [], len(matrix), len(matrix[0])
        for row in matrix:
            min_r.append(min(row))
        for i in range(y):
            temp = matrix[0][i]
            for j in range(x):
                temp = max(temp, matrix[j][i])
            max_c.append(temp)
        for i in range(len(max_c)):
            for j in range(len(min_r)):
                if max_c[i] == min_r[j]:
                    ans.append(min_r[j])
        return ans                
