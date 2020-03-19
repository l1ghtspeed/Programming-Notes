class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        def recurse(s, n, diff):
            if n == 0 and diff == 0:
                self.ans.append(s)
            if n > 0:
                recurse(s+'(', n-1, diff+1)
            if diff > 0:
                recurse(s+')', n, diff-1)
        recurse('', n, 0)
        return self.ans
