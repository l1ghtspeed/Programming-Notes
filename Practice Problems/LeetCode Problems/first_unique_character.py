from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = OrderedDict()
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]] = [i]
        for key in d:
            if len(d[key]) == 1:
                return d[key][0]
        return -1
