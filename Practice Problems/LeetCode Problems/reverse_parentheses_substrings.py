class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ')':
                stack.append(char)
            else:
                i = len(stack) - 1
                reverse = []
                while i > 0 and stack[i] != '(':
                    reverse.append(stack[i])
                    i -= 1
                stack = stack[:i] + reverse
        return ''.join(stack)
