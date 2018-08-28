#Solution times out on really large inputs, use dp or trie for faster runtime
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        stack = []
        stack.append(s)
        while stack:
            st = stack.pop()
            for item in wordDict:
                if len(item) <= len(st):
                    if st[:len(item)] == item:
                        stack.append(st[len(item):])
                elif len(st) == 0:
                    return True
        return False

 # DP method, very efficient

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(len(s)):
            if not dp[i]:
                continue
            for word in wordDict:
                length = len(word)
                end = i + length
                if end > len(s):
                    continue
                if dp[end]:
                    continue
                if s[i:end] == word:
                    dp[end] = True
        return dp[len(s)]
