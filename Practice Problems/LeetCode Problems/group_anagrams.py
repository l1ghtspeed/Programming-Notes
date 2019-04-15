def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        solutions = []
        
        d = {}
        for i in strs:
            if (i in d):
                d[i] = d[i] + 1
            else:
                d[i] = 1
        
        for key in d:
            tempSol = []
            tempSol.append(key)
            for key2 in d:
                if (key2 != key) and self.isAnagram(key, key2):
                    tempSol.append(key2)
                    del d[key2]
            solutions.append(tempSol)
            del d[key]
        
        return solutions
    
    def isAnagram(self, s1, s2):
        s_1 = [0]*26
        s_2 = [0]*26
        
        for i in range(len(s1)):
            pos = ord(s1[i])-ord('a')
            s_1[pos] = s_1[pos] + 1

        for i in range(len(s2)):
            pos = ord(s2[i])-ord('a')
            print(pos)
            print(s_2)
            s_2[pos] = s_2[pos] + 1

        for i in range(26):
            if s_1[i] != s_2[i]:
                return False

        return True