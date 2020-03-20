class Solution:
    def numTrees(self, n: int) -> int:
        memo = [1, 1, 2] + [0 for _ in range(n-2)]
    
        for i in range(3, n+1):
            for j in range(i):
                memo[i] += memo[j]*memo[i-j-1]
        
        return memo[n]
