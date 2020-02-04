class Solution:
    def removeDuplicates(self, S: str) -> str:
        ans = ''
        for char in S:
            if ans and char == ans[-1]:
                ans = ans[:-1]
            else:
                ans += char
        return ans
