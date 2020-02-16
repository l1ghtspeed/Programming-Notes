class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, ans = len(s), ('', 0)
        memo = [[0 for _ in range(l)] for _ in range(l)]
        for i in range(l):
            memo[i][i] = 1
        for i in range(l-1, -1, -1):
            for j in range(i+1, l):
                if s[i] == s[j] and ((memo[i+1][j-1] == 1 and memo[i+1][i+1] == 1) or j-i == 1):
                    memo[i][j] = 1
                    if ans[1] < j-i:
                        ans = (s[i:j+1], j-i)
        
        if ans[1] == 0 and s:
            return s[0]
        return ans[0]
