class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        memo = [[-1 for _ in range(k+1)] for _ in range(len(s))]
        def recurse(i, k):
            ans = None
            if memo[i][k] != -1:
                return memo[i][k]
            if k + i == len(s):
                ans = 0
            elif k == 1:
                ans = self.palindrome_helper(s[i:])
            else:
                paths = []
                j = i
                while k + j <= len(s):
                    j += 1
                    paths.append(self.palindrome_helper(s[i:j]) + recurse(j, k-1))
                ans = min(paths)
            memo[i][k] = ans
            return ans
        
        return recurse(0, k)
                
    def palindrome_helper(self, s):
        count = 0
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                count += 1
        return count
