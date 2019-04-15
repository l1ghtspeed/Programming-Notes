def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        substring = ''
        if strs:
            for i in range(len(strs[0])):
                for j in strs:
                    if i >= len(j):
                        return substring
                    elif strs[0][i] != j[i]:
                        return substring
                substring += strs[0][i]
        return substring