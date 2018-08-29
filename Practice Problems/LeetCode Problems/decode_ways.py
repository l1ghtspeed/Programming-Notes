class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        prev = 0
        cur = 0
        for char in range(len(s)):
            if s[char] == '0' and (char == 0 or (s[char-1] != '1' and s[char-1] != '2')):
                return 0
        if len(s) >= 2:
            l2 = int(s[-2:])
            if l2 <= 26 and l2 > 10 and l2 != 20:
                cur = 2
                prev = 1
            elif l2 <= 10 or l2 == 20:
                cur = 1
                prev = 0
            elif l2%10 == 0:
                return 0
            else:
                cur = 1
                prev = 1
            for i in range(len(s)-3, -1, -1):
                n = int(s[i:i+2])
                if n <= 26 and n > 10 and n != 20:
                    temp = cur
                    cur = cur + prev
                    prev = temp
                elif (n <= 10 and n > 0) or n == 20:
                    continue
                elif n%10 == 0:
                    return 0
                else:
                    prev = cur   
        else:
            return len(s)
        
        return cur
            
