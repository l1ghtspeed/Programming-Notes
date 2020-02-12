class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        count = 0
        for char in s:
            while j < len(t):
                if t[j] == char:
                    count += 1
                    j += 1
                    break
                j += 1
        if count == len(s):
            return True
        return False
            
