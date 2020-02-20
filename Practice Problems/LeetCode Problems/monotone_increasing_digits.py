class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = str(N)
        ans = ''
        for i in range(len(s)):
            if int(s[i]*(len(s)-i)) <= int(s[i:]):
                ans += s[i]
            else:
                ans += (str(int(s[i])-1) + '9'*(len(s)-i-1))
                return int(ans)
        return int(ans)
        
