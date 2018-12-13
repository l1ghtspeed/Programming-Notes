#Q771
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        s = set()
        for type in J:
            if type not in s:
                s.add(type)
        for type in S:
            if type in s:
                count += 1
        return count