class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        num_left, num_right = 0, 0
        for char in s:
            if char == '(': num_left += 1
            if char == ')':
                if num_left == 0:
                    num_right += 1
                else:
                    num_left -=1
        ans = set()
        def dfs(ind, left, right, num_left, num_right, path):
            if ind == len(s):
                if left == right and num_left == num_right == 0:
                    ans.add(path)
            else:
                if s[ind] == '(':
                    if num_left > 0:
                        dfs(ind + 1, left, right, num_left - 1, num_right, path)
                    dfs(ind + 1, left + 1, right, num_left, num_right, path+'(')
                elif s[ind] == ')':
                    if num_right > 0:
                        dfs(ind + 1, left, right, num_left, num_right - 1, path)
                    if left > right:
                        dfs(ind + 1, left, right + 1, num_left, num_right, path+')')
                else:
                    dfs(ind+1, left, right, num_left, num_right, path+s[ind])
        dfs(0, 0, 0, num_left, num_right, '')
        return ans
