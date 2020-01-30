class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        self.memo = [[-1 for _ in range(l2)] for _ in range(l1)]
        self.word1, self.word2 = word1, word2
        return self.recurse(l1-1, l2-1)
    
    def recurse(self, i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        ans = 0
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        if self.word1[i] == self.word2[j]:
            ans = self.recurse(i-1, j-1)
        else:
            ans = min(self.recurse(i-1, j), self.recurse(i, j-1), self.recurse(i-1, j-1)) + 1        
        self.memo[i][j] = ans
        return ans
    
