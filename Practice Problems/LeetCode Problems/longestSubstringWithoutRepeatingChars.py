def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ind = 0
        maxLen = 0
        currLen = 0
        seen = ''
        for i in range(len(s)):
            for j in range(ind, len(seen)):
                if (s[i] == seen[j]) and j >= ind:
                    ind = j+1
                    if currLen > maxLen:
                        maxLen = currLen
                    currLen = i-j-1
                    break
            seen += s[i]
            currLen += 1
        
        if currLen > maxLen:
            maxLen = currLen
        return maxLen
