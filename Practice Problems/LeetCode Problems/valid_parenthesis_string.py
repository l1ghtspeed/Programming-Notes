#TLEs
class Solution:
    def checkValidString(self, s: str) -> bool:
        def recurse(s, stack):
            for i in range(len(s)):
                char = s[i]
                if char == '(':
                    stack += 1
                elif char == ')':
                    if stack > 0:
                        stack -= 1
                    else:
                        return False
                else:
                    return recurse('(' + s[i+1:], stack) or recurse(')' + s[i+1:], stack) or recurse(s[i+1:], stack)
            return stack == 0
        
        return recurse(s, 0)
