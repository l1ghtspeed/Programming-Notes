class Solution:
    def minSteps(self, s: str, t: str) -> int:
#         update the freq map
        d1 = {}
        d2 = {}
        for i in s:
            if i not in d1:
                d1[i] = 0
            d1[i] += 1
        for j in t:
            if j not in d2:
                d2[j] = 0
            d2[j] += 1
            
            
        count = 0
        for elem in d1:
            if elem in d2:
                count += abs(d1[elem] - d2[elem])
            else:
                count += d1[elem]
        for elem2 in d2:
            if elem2 not in d1:
                count += d2[elem2]
        return math.ceil(count/2)
