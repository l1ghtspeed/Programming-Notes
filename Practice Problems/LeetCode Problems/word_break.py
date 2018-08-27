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
